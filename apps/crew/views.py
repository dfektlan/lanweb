from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings

from apps.crew.models import Application, CrewMember, CrewTeam
from apps.crew.forms import ApplicationAdminForm, ApplicationForm, RegisterRFIDForm, CreditToCrewForm, CrewCardForm, AddCrewMemberForm
from apps.event.models import LanEvent
from apps.userprofile.models import SiteUser
from apps.userprofile.views import profile
from apps.userprofile.templatetags.gravatar_url_resolver import get_gravatar_url

from PIL import Image, ImageFont, ImageDraw
import requests
from StringIO import StringIO
import zipfile
import os


@login_required
@user_passes_test(lambda u: u.is_chief())
def overview(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    #users_in_group = Group.objects.get(name="Core").siteuser_set.all()
    #groups = request.user.groups.all()
    #user = request.user
    #if user in users_in_group:
    #    pending = Application.objects.filter(status=0).order_by('-date')
    #    approved = Application.objects.filter(status=1).order_by('-date')
    #    declined = Application.objects.filter(status=2).order_by('-date')
    #else:
    pending = []
    approved = []
    declined = []
    for j in Application.objects.filter(event=eventObj).order_by('-date'):
        if j.status == 0:
            pending.append(j)
        elif j.status == 1:
            approved.append(j)
        elif j.status == 2:
            declined.append(j)
    return render(request, 'crew/overview.html', {'pending':pending, 'approved':approved,'declined':declined, 'event': event})


@login_required
@user_passes_test(lambda u: u.is_chief())
def look(request, event=None, application_id=None):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        form = ApplicationAdminForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            form.user = request.user
            if form.has_changed and form.cleaned_data['status'] == 1:
                add_to_crewteam(application_id, application.event)
            messages.success(request, u'The application was successfully saved')
            return redirect(overview)
        else:
            return HttpResponse('Invalid input')
    else:
        form = ApplicationAdminForm(instance=application)

    return render(request, 'crew/look.html', {"app": application, "form": form, 'event': event })


@login_required
def user_overview(request, event=None):
    apps = request.user.application_set.all().order_by('-date') 
    return render(request, 'crew/user_overview.html', {'apps': apps, 'event': event})


@login_required
def new_application(request, event=None, application_id=None):
    eventObj = LanEvent.objects.get(shortname=event)
    if application_id is None:
        application = Application()
    else:
        application = get_object_or_404(Application, pk=application_id)

    if request.POST:
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.user_id = request.user.id
            application.event = eventObj
            form.save()
            messages.success(request, u'Your application was succesfully submitted')
        return redirect(user_overview)
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'crew/new_application.html', {'form': form, 'event': event, })


def del_application(request, event=None, application_id=None):
    app = get_object_or_404(Application, pk=application_id)

    if app.user == request.user:
        app.delete()
        messages.success(request, u'The application has been deleted')
    else:
        messages.error(request, u'This is not your application, you cannot delete it')
    return redirect(profile)


@login_required
def crew(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    crewteams = CrewTeam.objects.all()
    currentCrewTeams = {}
    for team in crewteams:
        currentCrewTeams[team] = team.members.filter(event=eventObj)

    application_count = Application.objects.filter(event=eventObj).filter(status=0).count()
    return render(request, 'crew/crew.html', {'crewteams': currentCrewTeams, 'count': application_count, 'event': event})

@login_required
def crewteam(request, event=None, crewteam_id=None):
    eventObj = LanEvent.objects.get(shortname=event)
    crewteam = CrewTeam.objects.get(pk=crewteam_id)
    members = crewteam.members.filter(event=eventObj)
    return render(request, 'crew/crewteam.html', {'members': members, 'crewteam': crewteam, 'event': event})


@login_required
@user_passes_test(lambda u: u.is_chief())
def register_rfid(request, event=None):
    if request.POST:
        form = RegisterRFIDForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            if SiteUser.objects.filter(username=user.lower()).count() != 0:
                user = SiteUser.objects.get(username=user.lower())
                user.rfid = form.cleaned_data['rfid']
                user.save()
                messages.success(request, "RFID successfully updated")
            else:
                messages.error(request, "RFID unsuccessfully updated, %s does not exist." % user)
            return redirect(register_rfid)
        else:
            messages.error(request, "RFID unsuccessfully updated")
            return redirect(register_rfid)
    else:
        form = RegisterRFIDForm()

    return render(request, 'crew/register_rfid.html', {'form': form, 'event': event, })


@login_required
@user_passes_test(lambda u: u.is_chief())
def credit(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    if request.POST:
        form = CreditToCrewForm(request.POST, event=eventObj)
        if form.is_valid():
            if form.cleaned_data['all']:
                crewmembers = CrewMember.objects.filter(event=eventObj)
                for member in crewmembers:
                    member.add_credit(form.cleaned_data['credit'])
                messages.success(request, "The amount %s was added to every user for event %s" % (form.cleaned_data['credit'], eventObj.name))
            elif form.cleaned_data['crewmember']:
                for member in form.cleaned_data['crewmember']:
                    member.add_credit(form.cleaned_data['credit'])

                messages.success(request, "The amount %s was added to %s for event %s" % (form.cleaned_data['credit'], "selected users", eventObj.name))
            elif form.cleaned_data['crew']:
                for c in form.cleaned_data['crew']:
                    for member in c.members.all():
                        if member.event is eventObj:
                            member.add_credit(form.cleaned_data['credit'])
                messages.success(request, "The amount %s was added to %s for event %s" % (form.cleaned_data['credit'], "selected users", eventObj.name))

    else:
        form = CreditToCrewForm(event=eventObj)

    return render(request, 'crew/credit.html', {'form': form, 'event': event})


@login_required
@user_passes_test(lambda u: u.is_chief())
def credit_overview(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    crewteams = CrewTeam.objects.all()
    currentCrewTeams = {}
    for team in crewteams:
        currentCrewTeams[team] = team.members.filter(event=eventObj)
    return render(request, 'crew/credit_overview.html', {'crewteams': currentCrewTeams, 'event': event})


@login_required
@user_passes_test(lambda u: u.is_chief())
def crewcard(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    if request.POST:
        form = CrewCardForm(request.POST, event=eventObj)
        if form.is_valid():
            s = StringIO()
            zipp = zipfile.ZipFile(s, 'w')
            if form.cleaned_data['all']:
                crewmembers = CrewMember.objects.filter(event=eventObj)
                for member in crewmembers:
                    card = generate_crew_card(member.user)
                    zipp.writestr("%s_%s.jpg" % (member.user.first_name, member.user.last_name), card.getvalue())

            else:
                for member in form.cleaned_data['crewmember']:
                    card = generate_crew_card(member.user)
                    zipp.writestr("%s_%s.jpg" % (member.user.first_name, member.user.last_name), card.getvalue())

            #some fix for linux zip to windows
            for f in zipp.filelist:
                f.create_system = 0

            zipp.close()
            response = HttpResponse()
            response["Content-Disposition"] = "attachment; filename=crewcards.zip"
            response["Content-Type"] = "application/zip"

            s.seek(0)
            response.write(s.read())

            return response
    else:
        form = CrewCardForm(event=eventObj)

    return render(request, 'crew/crewcard.html', {'form': form, 'event': event})


@login_required
@user_passes_test(lambda u: u.is_chief())
def addcrewmember(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    if request.POST:
        form = AddCrewMemberForm(request.POST)
        if form.is_valid():
            for u in form.cleaned_data["users"]:
                crewmember = CrewMember(user=u, event=eventObj)
                crewmember.save()
                form.cleaned_data["crewteam"].members.add(crewmember)
        return redirect('addcrewmember', event=eventObj.shortname)

    else:
        form = AddCrewMemberForm()

    return render(request, "crew/addcrewmember.html", {'form': form, 'event': event })


def add_to_crewteam(aid, eventObj):
    user = Application.objects.get(pk=aid).user
    crew = Application.objects.get(pk=aid).crew
    crewmember = CrewMember.objects.get_or_create(user=user, event=eventObj)
    print(crewmember)
    if Application.objects.get(pk=aid).status == 1:
        crew.members.add(crewmember[0])


def check_for_application(user):
    if user.application_set.all():
        return user.application_set.all().latest()
    else:
        return None


def generate_crew_card(user):
    r = requests.get(get_gravatar_url("", user, 400))

    gravatar = Image.open(StringIO(r.content))
    template = Image.open(os.path.join(settings.MEDIA_ROOT, 'crewcard.jpg'))
    font = ImageFont.truetype(os.path.join(settings.MEDIA_ROOT, "Akashi.ttf"), 70)

    firstx, firsty = font.getsize(user.first_name)
    lastx, lasty = font.getsize(user.last_name)
    tempx, tempy = template.size
    x = (tempx / 2) - (firstx / 2)
    x2 = (tempx / 2) - (lastx / 2)

    draw = ImageDraw.Draw(template)

    draw.text((x, 430), user.first_name, (0, 0, 0), font=font)
    draw.text((x2, 430+firsty+10), user.last_name, (0, 0, 0), font=font)
    template.paste(gravatar, (119, 5))

    s = StringIO()

    template.save(s, format="jpeg")

    return s


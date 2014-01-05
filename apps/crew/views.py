from apps.crew.models import Application, CrewMember, CrewTeam
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from forms import ApplicationAdminForm, ApplicationForm
from django.contrib import messages
from django.http import HttpResponse
from apps.event.models import LanEvent


LATEST_EVENT = LanEvent.objects.filter(current=True)[0]

@login_required
@user_passes_test(lambda u: u.is_chief())
def overview(request):
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
    for j in Application.objects.all().order_by('-date'):
        if j.status == 0:
            pending.append(j)
        elif j.status == 1:
            approved.append(j)
        elif j.status == 2:
            declined.append(j)
    return render(request, 'crew/overview.html', {'pending':pending, 'approved':approved,'declined':declined})


@login_required
@user_passes_test(lambda u: u.is_chief())
def look(request, application_id=None):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        form = ApplicationAdminForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            form.user = request.user
            if form.has_changed and form.cleaned_data['status'] == 1:
                add_to_crewteam(application_id)
            messages.success(request, u'The application was successfully saved')
            return redirect(overview)
        else:
            return HttpResponse('Invalid input')
    else:
        form = ApplicationAdminForm(instance=application)

    return render(request, 'crew/look.html', {"app": application, "form": form })


@login_required
def user_overview(request):
    apps = request.user.application_set.all().order_by('-date') 
    return render(request, 'crew/user_overview.html', {'apps': apps})


@login_required
def new_application(request, application_id=None):
    if application_id is None:
        application = Application()
    else:
        application = get_object_or_404(Application, pk=application_id)

    if request.POST:
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.user_id = request.user.id
            application.event = LATEST_EVENT
            form.save()
            messages.success(request, u'Your application was succesfully submitted')
        return redirect(user_overview)
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'crew/new_application.html', {'form': form,})


def crew(request):
    crewteams = CrewTeam.objects.all()
    return render(request, 'crew/crew.html', {'crewteams': crewteams})


def crewteam(request, crewteam_id):
    crewteam = CrewTeam.objects.get(pk=crewteam_id)
    members = crewteam.members.all()
    return render(request, 'crew/crewteam.html', {'members': members, 'crewteam': crewteam})


def add_to_crewteam(aid):
    user = Application.objects.get(pk=aid).user
    crew = Application.objects.get(pk=aid).crew
    crewmember = CrewMember.objects.get_or_create(user=user, event=LATEST_EVENT)
    print(crewmember)
    if Application.objects.get(pk=aid).status == 1:
        crew.members.add(crewmember[0])


def check_for_application(user):
    if user.application_set.all():
        return user.application_set.all().latest()
    else:
        return None

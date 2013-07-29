from crew.models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from forms import ApplicationAdminForm, ApplicationForm
from django.contrib import messages

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Crew').count() == 1)
def overview(request):
    users_in_group = Group.objects.get(name="Core").siteuser_set.all()
    groups = request.user.groups.all()
    user = request.user
    if user in users_in_group:
        pending = Application.objects.filter(status=0).order_by('-date')
        approved = Application.objects.filter(status=1).order_by('-date')
        declined = Application.objects.filter(status=2).order_by('-date')
    else:
        pending = []
        approved = []
        declined = []
        for i in groups:
            for j in Application.objects.all().order_by('-date'):
                if j.get_crew_display() == i.name:
                    if j.status == 0:
                        pending.append(j)
                    elif j.status == 1:
                        approved.append(j)
                    elif j.status == 2:
                        declined.append(j)
    return render(request, 'crew/overview.html', {'pending':pending, 'approved':approved,'declined':declined})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Crew').count() == 1)
def look(request, application_id=None):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == "POST":
        form = ApplicationAdminForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            form.user = request.user
            if form.has_changed and form.cleaned_data['status'] == 1:
                change_group(application_id)
                add_to_crew(application_id)
            messages.success(request, u'The application was successfully saved')
            return redirect(overview)
        else:
            return HttpResponse('Invalid input')
    else:
        form = ApplicationAdminForm(instance=application)

    return render(request, 'crew/look.html', {"app" : application, "form" : form })

@login_required
def user_overview(request):
    apps = request.user.application_set.all().order_by('-date') 
    return render(request, 'crew/user_overview.html', {'apps' : apps})

@login_required
def new_application(request, application_id=None):
    if application_id == None:
        application = Application()
    else:
        application = get_object_or_404(Application, pk=application_id)

    if request.POST:
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application.user_id = request.user.id
            form.save()
            messages.success(request, u'Your application was succesfully submitted')
        return redirect(user_overview)
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'crew/new_application.html', {'form':form,})

def change_group(aid):
    user = Application.objects.get(pk=aid).user 
    if Application.objects.get(pk=aid).status == 1:
       crew = Group.objects.get(name="Crew")
       crew.siteuser_set.add(user)

def add_to_crew(aid): 
    user = Application.objects.get(pk=aid).user
    crew = Application.objects.get(pk=aid).crew
    if Application.objects.get(pk=aid).status == 1:
        user.crew.add(crew.crewshift_set.get(name="Flexi"))
        

def check_for_application(user):
    if user.application_set.all():
        return user.application_set.all().latest()
    else:
        return None

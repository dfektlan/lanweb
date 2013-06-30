from crew.models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from forms import ApplicationAdminForm, ApplicationForm

#def index(request):

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Crew').count() == 1)
def overview(request):
    users_in_group = Group.objects.get(name="Core").siteuser_set.all()
    groups = request.user.groups.all()
    user = request.user
    if user in users_in_group:
        pending = Application.objects.filter(status=0)
        approved = Application.objects.filter(status=1)
        declined = Application.objects.filter(status=2)
    else:
        pending = []
        approved = []
        declined = []
        for i in groups:
            for j in Application.objects.all():
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
            if form.has_changed:
                change_group(application_id)
            #return validate_request(request, form)
            print dir(form)
        else:
            return HttpResponse('Invalid input')
    else:
        form = ApplicationAdminForm(instance=application)

    return render(request, 'crew/look.html', {"app" : application, "form" : form })

@login_required
def user_overview(request):
    apps = request.user.application_set.all() 
    return render(request, 'crew/user_overview.html', {'apps' : apps})

def change_group(aid):
    u = Application.objects.get(pk=aid).user 
    if Application.objects.get(pk=aid).status == 1:
       app_crew = Group.objects.get(name=Application.objects.get(pk=aid).get_crew_display())
       crew = Group.objects.get(name="Crew")
       for i in u.groups.all():
           Group.objects.get(id=i.id).siteuser_set.remove(u)
       app_crew.siteuser_set.add(u)
       crew.siteuser_set.add(u)
    else: 
       for i in u.groups.all():
           Group.objects.get(id=i.id).siteuser_set.remove(u)
       d = Group.objects.get(name='Deltager').siteuser_set.remove(u)



def check_for_application(user):
    if user.application_set.all():
        return user.application_set.all().latest()
    else:
        return None

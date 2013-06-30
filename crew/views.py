from crew.models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

#def index(request):

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Crew').count() == 1)
def applications_view(request):
    users_in_group = Group.objects.get(name="Core").siteuser_set.all()
    groups = request.user.groups.all()
    user = request.user
    if user in users_in_group:
        apps = Application.objects.filter(status=0)
    else:
        apps = []
        for i in groups:
            for j in Application.objects.filter(status=0):
                if j.get_crew_display() == i.name:
                    apps.append(j)
    return render(request, 'crew/applications.html', {'apps':apps})


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Crew').count() == 1)
def application(request):
    test = "lol"

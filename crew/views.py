from crew.models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

#def index(request):

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Crew').count() == 1)
def applications(request):
    groups = request.user.groups.all()
    print groups
    apps = []
    for i in groups:
        for j in Application.objects.filter(status=0):
            if j.get_crew_display() == i.name:
                apps.append(j)
    applications = Application.objects.filter(status=0)
    return render(request, 'crew/applications.html', {'apps':apps})

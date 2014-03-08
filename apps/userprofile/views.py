from apps.userprofile.models import SiteUser
from django.shortcuts import render, get_object_or_404, redirect


def profile(request, user_id=None):
    if user_id == None:
        user = request.user
    else:
        user = SiteUser.objects.get(id=user_id)
    apps = user.application_set.all()
    attended = get_all_attended_events(user)

    return render(request, 'userprofile/profile.html', {'user': user, 'apps': apps, 'attended': attended})


def get_all_attended_events(user):
    events_as_crew = user.crewmember_set.all()
    return events_as_crew
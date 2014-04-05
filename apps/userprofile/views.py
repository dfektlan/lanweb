from django.contrib.auth.decorators import login_required
from django.http import Http404
from apps.userprofile.models import SiteUser
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def profile(request, user_id=None):
    if user_id == None:
        raise Http404
    else:
        user = SiteUser.objects.get(id=user_id)
    apps = user.application_set.all()
    attended = get_all_attended_events(user)

    return render(request, 'userprofile/profile.html', {'profile': user, 'apps': apps, 'attended': attended})

@login_required
def myprofile(request):
    user = request.user
    apps = user.application_set.all()
    attended = get_all_attended_events(user)

    return render(request, 'userprofile/myprofile.html', {'user': user, 'apps': apps, 'attended': attended})


def get_all_attended_events(user):
    events_as_crew = user.crewmember_set.all()
    return events_as_crew
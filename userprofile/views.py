from userprofile.models import SiteUser
from crew.models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def profile(request, user_id=None):
    if user_id == None:
        user = request.user
    else:
        user = SiteUser.objects.get(id=user_id)
    apps = user.application_set.all()
    return render(request, 'userprofile/profile.html', {'user':user, 'apps':apps})

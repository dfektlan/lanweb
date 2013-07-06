from userprofile.models import SiteUser
from crew.models import Application
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def myprofile(request):
    user = request.user
    apps = user.application_set.all()
    return render(request, 'userprofile/myprofile.html', {'user':user, 'apps':apps})

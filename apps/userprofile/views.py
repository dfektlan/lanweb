from django.contrib.auth.decorators import login_required
from django.http import Http404
from apps.userprofile.forms import EditProfileForm
from apps.userprofile.models import SiteUser
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def profile(request, event=None, user_id=None):
    user = get_object_or_404(SiteUser, id=user_id)
    apps = user.application_set.all()
    attended = get_all_attended_events(user)

    return render(request, 'userprofile/profile.html', {'profile': user, 'apps': apps, 'attended': attended, 'event': event})


@login_required
def myprofile(request, event=None):
    user = request.user
    apps = user.application_set.all()
    attended = get_all_attended_events(user)

    return render(request, 'userprofile/myprofile.html', {'user': user, 'apps': apps, 'attended': attended, 'event': event})


@login_required
def edit_profile(request, event=None):
    user = request.user
    if request.POST:
        form = EditProfileForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            user.first_name = cleaned["first_name"]
            user.last_name = cleaned["last_name"]
            user.email = cleaned["email"]
            user.address = cleaned["address"]
            user.zip_code = cleaned["zip_code"]
            user.town = cleaned["town"]
            user.country = cleaned["country"]
            user.phone = cleaned["phone"]
            user.skype = cleaned["skype"]
            user.steam = cleaned["steam"]
            user.save()
            user.setNameNotRetard()
            return redirect(myprofile, event=event)
    else:
        form = EditProfileForm(initial={
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address": user.address,
            "zip_code": user.zip_code,
            "town": user.town,
            "country": user.country,
            "phone": user.phone,
            "skype": user.skype,
            "steam": user.steam
        })
    return render(request, 'userprofile/editprofile.html', {'form': form, 'user': user, 'event': event})



def get_all_attended_events(user):
    events_as_crew = user.crewmember_set.all()
    return events_as_crew

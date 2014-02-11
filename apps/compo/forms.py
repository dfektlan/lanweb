# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from apps.compo.models import Participant
from apps.userprofile.models import SiteUser

dummy = []

class RegisterTeamForm(forms.Form):
    teamname = forms.CharField(label='Lagnavn', max_length=30)
    username = forms.ModelMultipleChoiceField(dummy)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(RegisterTeamForm, self).__init__(*args, **kwargs)
        unwanted_users = []
        unwanted_users.append(self.request.user)
        for user in SiteUser.objects.all():
            if user.is_teamleader.all() or user.is_teammember.all():
                unwanted_users.append(user)
        self.fields["username"].queryset = SiteUser.objects.exclude(id__in=[o.id for o in unwanted_users])
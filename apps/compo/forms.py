# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from apps.userprofile.models import SiteUser

class RegisterTeamForm(forms.Form):
    username = forms.ModelChoiceField(SiteUser.objects.all(), label='Brukernavn')
    teamname = forms.CharField(label='Lagnavn', max_length=30)
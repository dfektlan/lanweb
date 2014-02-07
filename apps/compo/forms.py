# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from apps.compo.models import Participant
from apps.userprofile.models import SiteUser

#USERS = []
#for user in SiteUser.objects.all():
#    USERS.append(user)

class RegisterTeamForm(forms.Form):
    teamname = forms.CharField(label='Lagnavn', max_length=30)
    username = forms.ModelMultipleChoiceField(SiteUser.objects.all())
    #username = forms.ModelChoiceField(SiteUser.objects.all(), label='Brukernavn')
    #username = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=USERS)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(RegisterTeamForm, self).__init__(*args, **kwargs)
        self.fields["username"].queryset = SiteUser.objects.exclude(pk=self.request.user.pk)
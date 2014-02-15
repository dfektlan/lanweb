# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from apps.compo.models import Participant
from apps.userprofile.models import SiteUser
from apps.compo.models import Team

dummy = []


class RegisterTeamForm(ModelForm):
    #teamname = forms.CharField(label='Lagnavn', max_length=30)
    #username = forms.ModelMultipleChoiceField(dummy)
    class Meta:
        model = Team
        exclude = ('teamleader',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        tour = kwargs.pop("tour")
        super(RegisterTeamForm, self).__init__(*args, **kwargs)
        unwanted_users = [self.request.user]
        for user in SiteUser.objects.all():
            if user.is_teamleader.filter(participant__tournament=tour) or \
                    user.is_teammember.filter(participant__tournament=tour):
                unwanted_users.append(user)
        self.fields['members'].queryset = SiteUser.objects.exclude(id__in=[o.id for o in unwanted_users])
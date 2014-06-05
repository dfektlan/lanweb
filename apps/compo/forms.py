# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from apps.userprofile.models import SiteUser
from apps.compo.models import Team

dummy = []


class RegisterTeamForm(ModelForm):
    # teamname = forms.CharField(label='Lagnavn', max_length=30)
    # username = forms.ModelMultipleChoiceField(dummy)
    # action_url = 'add_team'
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


class ChallongeForm(forms.Form):
    initial = 0
    CHOICES = (
        (u'single elimination', u'single elimination'),
        (u'double elimination', u'double elimination'),
        (u'round robin', u'round robin'),
        (u'swiss', u'swiss'),
    )
    type = forms.ChoiceField(choices=CHOICES, label="Challonge-type")


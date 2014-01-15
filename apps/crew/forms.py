from django import forms
from django.forms import ModelForm, Form
from models import Application
from apps.userprofile.models import SiteUser
import re

class ApplicationAdminForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'about', 'why', 'license', 'date', 'cv')


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('status', 'date', 'user', 'event')


class RegisterRFIDForm(Form):
    username = forms.CharField(label="Brukernavn", max_length=20)
    rfid = forms.CharField(label="RFID", max_length=30)

    def is_valid(self):
        super(RegisterRFIDForm, self).is_valid()
        clean = self.cleaned_data

        if SiteUser.objects.filter(nickname=clean.username).count() != 1:
            return False

        if not re.match('[0-9]', clean.rfid):
            return False

        return True
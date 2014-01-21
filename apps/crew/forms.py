from django import forms
from django.forms import ModelForm
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


class RegisterRFIDForm(forms.Form):
    username = forms.CharField(label="Brukernavn", max_length=20)
    rfid = forms.CharField(label="RFID", max_length=30)


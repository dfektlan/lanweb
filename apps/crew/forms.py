from django import forms
from django.forms import ModelForm
from models import Application, CrewMember, CrewTeam
from apps.event.models import LanEvent

LATEST_EVENT = LanEvent.objects.filter(current=True)[0]


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
    rfid = forms.CharField(label="RFID", max_length=20)

    def is_valid(self):
        valid = super(RegisterRFIDForm, self).is_valid()

        if not valid:
            return valid

        if not self.cleaned_data['rfid'].isdigit():
            return False

        return True


class CreditToCrewForm(forms.Form):
    #crewmember = forms.ModelChoiceField(CrewMember.objects.all(), label="Crewmedlem", required=False)
    crewmember = forms.ModelMultipleChoiceField(CrewMember.objects.filter(event=LATEST_EVENT), label="Crewmedlem", required=False)
    crew = forms.ModelMultipleChoiceField(CrewTeam.objects.all(), label="Crew", required=False)
    all = forms.BooleanField(label="Alle crew medlemmer?", required=False)
    credit = forms.IntegerField(label="Gatepoeng")


class CrewCardForm(forms.Form):
    crewmember = forms.ModelMultipleChoiceField(CrewMember.objects.filter(event=LATEST_EVENT), label="Crewmedlem", required=False)
    all = forms.BooleanField(label="Alle crew medlemmer?", required=False)






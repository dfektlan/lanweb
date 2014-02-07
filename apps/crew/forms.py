from django import forms
from django.forms import ModelForm
from models import Application, CrewMember


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
    crewmember = forms.ModelChoiceField(CrewMember.objects.all(), label="Crewmedlem")
    all = forms.BooleanField(label="Alle crew medlemmer?", required=False)
    credit = forms.IntegerField(label="Kredit")





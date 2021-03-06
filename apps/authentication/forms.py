# -*- coding: utf-8 -*-

import datetime
import re

from django import forms
from django.contrib import auth
from apps.userprofile.models import SiteUser


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label="Brukernavn", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Passord")
    user = None

    def clean(self):
        if self._errors:
            return

        user = auth.authenticate(username=self.cleaned_data['username'].lower(), password=self.cleaned_data['password'])

        if user:
            if user.is_active:
                self.user = user
            else:
                self._errors['username'] = self.error_class(["Your account is inactive, try to recover it."])
        else:
            self._errors['username'] = self.error_class(["The account does not exist, or username/password combination is incorrect."])
        return self.cleaned_data

    def login(self, request):
        try:
            SiteUser.objects.get(username=request.POST['username'].lower())
        except:
            return False
        if self.is_valid():
            auth.login(request, self.user)
            request.session.set_expiry(0)
            return True
        return False


class RegisterForm(forms.Form):
    username = forms.CharField(label="Brukernavn", max_length=20)
    first_name = forms.CharField(label="Fornavn", max_length=50)
    last_name = forms.CharField(label="Etternavn", max_length=50)
    date_of_birth = forms.DateField(label=u"Fødselsdag", initial=datetime.datetime.now().__format__('%d/%m/%Y'), input_formats=['%d/%m/%Y', '%d/%m/%y', '%d.%m.%y', '%d.%m.%Y', ], widget=forms.TextInput(attrs=
        {
            'id': 'datepicker',
            'class': 'date',
            'data-provide': 'datepicker',
            'data-date-format': 'dd/mm/yyyy'
        }))
    email = forms.EmailField(label="Epost", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Passord")
    repeat_password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Gjenta passord")
    address = forms.CharField(label="Adresse", max_length=50)
    zip_code = forms.CharField(label="Postnummer", max_length=4)
    town = forms.CharField(label="By", max_length=20)
    country = forms.CharField(label="Land", max_length=20, initial="Norge")
    phone = forms.CharField(label="Telefonnummer", max_length=20)
    skype = forms.CharField(label="Skype", max_length=20, required=False)
    steam = forms.CharField(label="Steam", max_length=20, required=False)

    def clean(self):
        super(RegisterForm, self).clean()
        if self.is_valid():
            cleaned_data = self.cleaned_data

            # Check date of birth
            # currently only checks that it is not after today
            date = cleaned_data['date_of_birth']
            if date >= datetime.date.today():
                self._errors['date_of_birth'] = self.error_class(["You seem to be from the future, please enter a more believable date of birth."])

            # Check passwords
            if cleaned_data['password'] != cleaned_data['repeat_password']:
                self._errors['repeat_password'] = self.error_class(["Passwords did not match."])

            # Check username
            username = cleaned_data['username']
            if SiteUser.objects.filter(username=username).count() > 0:
                self._errors['username'] = self.error_class(["There is already a user with that username."])
            if not re.match("^[a-zA-Z0-9_-]+$", username):
                self._errors['username'] = self.error_class(["Your desired username contains illegal characters. Valid: a-Z 0-9 - _"])

            # Check email
            email = cleaned_data['email']
            if SiteUser.objects.filter(email=email).count() > 0:
                self._errors['email'] = self.error_class(["There is already a user with that email."])

            # ZIP code digits only
            zip_code = cleaned_data['zip_code']
            if len(zip_code) != 4 or not zip_code.isdigit():
                self._errors['zip_code'] = self.error_class(["The ZIP code must be 4 digit number."])

            return cleaned_data


class RecoveryForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Old password", required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="New password")
    repeat_password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="Repeat new password")

    def clean(self):
        super(ChangePasswordForm, self).clean()
        if self.is_valid():
            cleaned_data = self.cleaned_data

            # Check passwords
            if cleaned_data['new_password'] != cleaned_data['repeat_password']:
                self._errors['repeat_password'] = self.error_class(["Passwords did not match."])

            return cleaned_data

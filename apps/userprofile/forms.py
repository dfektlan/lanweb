from django import forms
from apps.userprofile.models import SiteUser


class EditProfileForm(forms.Form):
    first_name = forms.CharField(label="Fornavn", max_length=50)
    last_name = forms.CharField(label="Etternavn", max_length=50)
    email = forms.EmailField(label="Epost", max_length=50)
    address = forms.CharField(label="Adresse", max_length=50)
    zip_code = forms.CharField(label="Postnummer", max_length=4)
    town = forms.CharField(label="By", max_length=20)
    country = forms.CharField(label="Land", max_length=20, initial="Norge")
    phone = forms.CharField(label="Telefonnummer", max_length=20)
    skype = forms.CharField(label="Skype", max_length=20, required=False)
    steam = forms.CharField(label="Steam", max_length=20, required=False)

    def clean(self):
        super(EditProfileForm, self).clean()
        if self.is_valid():
            cleaned_data = self.cleaned_data

            # Check email
            email = cleaned_data['email']
            if SiteUser.objects.filter(email=email).count() > 1:
                self._errors['email'] = self.error_class(["There is already a user with that email."])

            # ZIP code digits only
            zip_code = cleaned_data['zip_code']
            if len(zip_code) != 4 or not zip_code.isdigit():
                self._errors['zip_code'] = self.error_class(["The ZIP code must be 4 digit number."])

            return cleaned_data


from django import forms
from django.contrib.auth.forms import UserCreationForm

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "license_number"
        )


class LicenceForm(forms.ModelForm):
    NUM_OF_DIGITS = 8
    license_number = forms.CharField(required=True)

    class Meta:
        model = Driver
        fields = ("license_number",)


class DriverLicenceUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

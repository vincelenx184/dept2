from django import forms
from .models import StaffProfile


class StaffProfileCreateForm(forms.ModelForm):

    class Meta:
        model = StaffProfile
        fields = [
            "first_name",
            "last_name",
        ]


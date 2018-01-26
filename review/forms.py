from django import forms
from staff.models import StaffProfile
from .models import Appraisal


class AppraisalForm(forms.ModelForm):
    class Meta:
        model = Appraisal
        fields = [
            "employee",
            "overall_rating",
            "positive_qualities",
            "negative_qualities",
            "public",

        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super().__init__(*args, **kwargs)
        self.fields["employee"].queryset = StaffProfile.objects.filter(owner=user) #.exclude(appraisal__isnull=False)










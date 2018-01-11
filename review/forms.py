from django import forms

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
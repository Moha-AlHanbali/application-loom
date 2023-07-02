from django import forms

from .models import Interaction, Location, Application


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ["interaction_date", "interaction_description"]
        widgets = {"interaction_date": forms.widgets.DateInput(attrs={"type": "date"})}


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["country", "city", "address"]


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "application_date",
            "application_status",
            "post_url",
            "company_name",
            "job_title",
            "job_role_and_responsibilities",
            "job_requirements",
            "job_benefits",
            "work_model",
            "notes",
        ]
        widgets = {"application_date": forms.widgets.DateInput(attrs={"type": "date"})}
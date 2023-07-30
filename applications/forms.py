from django import forms
from .models import CareerBoard, Interaction, Application


class CareerBoardForm(forms.ModelForm):
    class Meta:
        model = CareerBoard
        fields = ['name']


        
class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = [
            "interaction_highlight",
            "interaction_date",
            "interaction_description",
        ]
        widgets = {"interaction_date": forms.widgets.DateInput(attrs={"type": "date"})}


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "application_date",
            "application_status",
            "post_url",
            "company_name",
            "job_title",
            "job_country",
            "job_city",
            "job_address",
            "job_role_and_responsibilities",
            "job_requirements",
            "job_benefits",
            "work_model",
            "notes",
        ]
        widgets = {"application_date": forms.widgets.DateInput(attrs={"type": "date"})}
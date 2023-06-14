from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'


class InsightsForm(forms.Form):
    CHOICES = [
    ('choices--choices-multiple-remove-button-item-choice-10', 'Engineering'),
    ('choices--choices-multiple-remove-button-item-choice-19', 'IT & Telecoms') 
    ]
        
    industry = forms.ChoiceField(label="Industry", choices=CHOICES)
    job_description = forms.CharField(label="Job Description")
    cv_content = forms.CharField(label="CV Content")
    # https://cvscan.uk/
    def get_match_percentage(self):
        return
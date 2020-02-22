from .models import ProjectSubmission
from django import forms

class ProjectSubmissionForm(forms.ModelForm):
    class Meta:
        model = ProjectSubmission
        fields = '__all__'
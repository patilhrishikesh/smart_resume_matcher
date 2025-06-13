from django import forms
from .models import Resume

class Resumeform(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'file']
        
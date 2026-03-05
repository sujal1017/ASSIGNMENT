from django import forms
from .models import stuDB

class StudentForm(forms.ModelForm):
    class Meta:
        model = stuDB
        fields = ['name', 'USN']
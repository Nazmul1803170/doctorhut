from .models import DoctorList
from django import forms

class addDoctor(forms.ModelForm):
    class Meta:
        model = DoctorList
        fields = '__all__'

from django import forms
from django.forms import ModelForm

from .models import VaccineRegistration

class VaccineRegistrationForm(forms.ModelForm):
    class Meta:
        model = VaccineRegistration
        fields = ['name', 'address', 'mobile', 'nid', 'p_vac']
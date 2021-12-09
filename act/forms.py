from django.forms.models import ModelForm
from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ("a_name","a_number", "a_material")

       
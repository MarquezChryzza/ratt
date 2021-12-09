from django import forms
from django.forms import widgets
from .models import VideoFiles
from django.forms.models import ModelForm
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model= VideoFiles
        fields= ["title","activity_number", "video"]


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_number': forms.Select(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'})
        }

from django import forms
from .models import Properties

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['name', 'description', 'image', 'url']
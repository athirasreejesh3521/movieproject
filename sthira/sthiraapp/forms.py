from django import forms
from . models import Service

class Serviceform(forms.ModelForm):
    class Meta:
        model=Service
        fields=['type','desc','img']

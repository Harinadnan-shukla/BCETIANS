from django import forms  
from .models import SignUpForm,EventAlumniMeet

class SignUpFormForm(forms.ModelForm):
    class Meta:
        model=SignUpForm
        fields="__all__"

class EventAlumnimeetform(forms.ModelForm):
    class Meta:
        model=EventAlumniMeet
        fields="__all__"




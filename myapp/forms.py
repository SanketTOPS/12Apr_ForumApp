from dataclasses import fields
from pyexpat import model
from django import forms
from .models import user_signup,mynotes,feedback

class SignupForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'
    
class NotesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields="__all__"

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'



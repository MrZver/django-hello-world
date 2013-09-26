from django import forms
from django.forms import ModelForm
from app.models import User, Message


# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField()
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

class ContactForm(ModelForm):
    class Meta:
        model = User
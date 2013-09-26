from django import forms
from django.forms import ModelForm
from app.models import User1


class ContactForm(ModelForm):
    class Meta:
        model = User1
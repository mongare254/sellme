from django import forms
from django.forms import ModelForm
from .models import  User, Profile
from django.contrib.auth.models import User

class UpdateForm(ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'


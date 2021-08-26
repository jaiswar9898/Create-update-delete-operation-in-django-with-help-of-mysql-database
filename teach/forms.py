from django import forms 

from django.forms import ModelForm, Textarea, widgets
from django import forms 
from .models import Employee
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#forms.ModelForm is for inheritance which inheritate from from django.forms import ModelForm 

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"




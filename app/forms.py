from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor

class PatientSignUpForm(UserCreationForm):

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode']

class DoctorSignUpForm(UserCreationForm):

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode']


from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from voters.models import PersonRegistration

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image','email','first_name','last_name','id_type','identification','birthPlace','birthDate',
                  'address','city','state','zipCode','gender','telp','marital_status']

class VoterRegistrationForm(forms.ModelForm):
    class Meta:
        model = PersonRegistration
        fields = ['voting_method']

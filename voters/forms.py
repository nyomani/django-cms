from django import forms
from .models import PersonRegistration

class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonRegistration
        fields = '__all__'

        widgets={
            'identification':forms.TextInput(
                attrs={'class':'form-control',
                       'placeholder':'Enter your passport no',
                       'validation':'Passport no is required',}
            ),
            'first_name':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your first name'}
            ),
            'last_name':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your last name'}
            ),
            'birthPlace':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your birth place'}
            ),
            'birthDate':forms.DateInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your birth date'}
            ),
            'address':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your street and no'}
            ),
            'city':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your city'}
            ),
            'state':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your state'}
            ),
            'zipCode':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your zip code'}
            ),
            'email':forms.EmailInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your email'}
            ),
            'telp':forms.TextInput(
                attrs={'class':'form-control','required':True,'placeholder':'Enter your Telp no.'}
            ),
            'gender':forms.Select(
                attrs={'class':'form-control','placeholder':''}
            ),
            'marital_status':forms.Select(
                attrs={'class':'form-control','placeholder':''}
            ),
            'disability':forms.Select(
                attrs={'class':'form-control','placeholder':''}
            ),
        }
        labels={
            'identification':'Passport No',
            'first_name':'First Name',
            'last_ame':'Last Name',
            'birthPlace':'Birth Place',
            'birthDate':'Birth Date',
            'address':'Street',
            'city':'City',
            'zipCode':'ZIP Code',
            'email':'Email',
            'telp':'Telp',
            'gender':'Gender',
            'marital_status':'Marriage Status',
            'disability':'Disability'
        }     

class PassportUpload(forms.Form):
    file = forms.FileField()

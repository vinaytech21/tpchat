from django import forms
 #from registration.forms import RegistrationForm
from django import forms

 
class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

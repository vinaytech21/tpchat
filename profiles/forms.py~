from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            Field('zipfield'),
            )

    class Meta:
        model = User
        fields = ['name','zipfield']



class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('picture'),
            Field('bio'),
            Field('zipcode'),

            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio','zipcode']


class SignupForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name')
    zipfield = forms.CharField(max_length=30, label='Zipcode')

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.zipfield = self.cleaned_data['zipfield']
        user.save()

    

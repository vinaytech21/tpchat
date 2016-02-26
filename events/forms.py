from django import forms
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from events.models import Event

class EventForm(forms.Form):
    eventtype = forms.CharField(required=False,label='Title', widget=forms.TextInput(attrs={'placeholder': 'Title of event'}))
    snap = forms.FileField(required=False,label='Event Look-up Picture ')    
    date_event = forms.DateTimeField(label='Event Date',widget=DateTimeWidget(usel10n=True, bootstrap_version=3))    
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'placeholder': 'Give some overview of your event'}))
    place = forms.CharField(
        label='Place', widget=forms.TextInput(attrs={'placeholder': 'Location of your event offer '})
    )    
    duration = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))
    dresscode = forms.BooleanField(
        label='Event Dress Code Allow'
    )  

class HostForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('eventtype', 'snap', 'date_event', 'description','place', 'dresscode', 'duration', )
  
    
    

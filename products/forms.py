from django import forms
from django.contrib.auth.models import User
from products.models import Product
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'quantity','address', 'zip_Code', 'expire_date', )


class ProductForm(forms.Form):
    
    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    )
    
    description = forms.CharField(
        label='Description', widget=forms.TextInput(attrs={'placeholder': 'Tell more about your donating item'})
    )   
   
    quantity = forms.IntegerField(
        label='Quantity', widget=forms.TextInput(attrs={'placeholder': 'No. of items you donating'})
    )
    zip_Code = forms.CharField(
        label='Zipcode', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )
    docfile = forms.FileField(
        label='Product Image '
    )
    address = forms.CharField(
        label='Place Where Available', widget=forms.TextInput(attrs={'placeholder': 'Your loaction where item available '})
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish'
    )



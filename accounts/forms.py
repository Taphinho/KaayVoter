from django import forms
from .models import User

class AuthenticationForm(forms.Form):
    #class Meta:
        #model = User
        #fields = ['prénom', 'nom', 'NIN']
    prenom = forms.CharField(
        label_suffix='', 
        label='Prénom*', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control search'})
    )
    nom = forms.CharField(
        label_suffix='', 
        label='Nom', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control search'})
    )
    nin = forms.CharField(
        label_suffix='', 
        label='NIN', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control search'})
    )

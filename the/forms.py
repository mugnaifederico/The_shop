from django import forms
from django.forms import ModelForm 
from .models import The

class addThe(ModelForm):
    
    class Meta:
        model = The
        fields = ['nome', 'descrizione', 'provenienza', 'immagine']
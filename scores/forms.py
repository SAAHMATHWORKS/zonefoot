from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class DateInput(forms.DateInput):
    input_type = 'date'




#Buteurs
class ButForm(forms.ModelForm):
    class Meta:
        model = But
        fields = ('match', 'player', 'minute',)
        
        labels = {
            "match": "Match",
            "player": "Joueur",
            "minute": "Minute",
        }
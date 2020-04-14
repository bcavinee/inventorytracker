from django import forms
from .models import Chemistry_Inventory, Hematology_Inventory

class HematologyCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Hematology_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

class ChemistryCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Chemistry_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

from django import forms
from .models import Hematology_Inventory, Chemistry_Inventory, Endo_Inventory, Coagulation_Inventory, GasesMetals_Inventory, Urines_Inventory
class HematologyCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Hematology_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

class ChemistryCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Chemistry_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

class EndoCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Endo_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

class UrinesCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Urines_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

class GasesMetalsCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= GasesMetals_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)

class CoagulationCheckoutForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Coagulation_Inventory.objects.all(), empty_label='Choose Reagent')
    amount_taken= forms.IntegerField(min_value=0)


#Average Use Playing

class DateInput(forms.DateInput):
    input_type= 'date'

class HematologyAverageUseForm(forms.Form):

    reagent_name= forms.ModelChoiceField(queryset= Hematology_Inventory.objects.all(), empty_label='Choose Reagent')
    start_date= forms.DateField(widget=DateInput)
    end_date= forms.DateField(widget=DateInput)
    #download_all_reagent_data= forms.BooleanField(required= False)

class HematologyDownloadAll(forms.Form):

    start_date= forms.DateField(widget=DateInput)
    end_date= forms.DateField(widget=DateInput)





#ONE TO ONE RELATIONSHIP FORMS

# class HematologyOneTestForm(forms.Form):
#
#     reagent_name= forms.ModelChoiceField(queryset= Heme_Test.objects.all(), empty_label='Choose Reagent')
#     amount_taken= forms.IntegerField(min_value=0)

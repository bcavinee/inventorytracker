from django.shortcuts import render
from .models import Hematology_Inventory, Chemistry_Inventory, Endo_Inventory, Coagulation_Inventory, GasesMetals_Inventory, Urines_Inventory
from django.views.generic import ListView, TemplateView
from django_tables2 import SingleTableView
from .tables import HematologyTable, ChemistryTable, EndoTable, CoagulationTable, GasesMetalsTable, UrinesTable
from .forms import HematologyCheckoutForm, ChemistryCheckoutForm, UrinesCheckoutForm, CoagulationCheckoutForm, EndoCheckoutForm, GasesMetalsCheckoutForm
from django.db.models import F
from django_tables2 import SingleTableView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def home(request):

    return render(request,'inventoryhome/home.html')

def about(request):
    return render(request,'inventoryhome/about.html', {'title' : 'about'})

@login_required(login_url='/login/')
def hematology(request):

    return render(request,'inventoryhome/hematology.html')


class HematologyListView(SingleTableView):

     model= Hematology_Inventory
     table_class= HematologyTable
     template_name= 'inventoryhome/hematology_inventory.html'

def hematology_checkout(request):


    if request.method == 'POST':
        form= HematologyCheckoutForm(request.POST)

        if form.is_valid():

            reagent_name= form.cleaned_data['reagent_name']
            amount_taken= form.cleaned_data['amount_taken']
        # get the reagent object
            reagent = Hematology_Inventory.objects.get(reagent_name=reagent_name)
        # reduce quantity
            reagent.reagent_quantity -= amount_taken
        # save the object
            reagent.save()
            messages.success(request, '***Reagent Removed From Inventory***')
            if reagent.reagent_quantity <= 0:
                messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')

    form= HematologyCheckoutForm()
    return render(request,'inventoryhome/hematology_reagent_checkout.html', {'form' : form})

class HematologyChartView(TemplateView):

    template_name= 'inventoryhome/hematologychart.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['qs'] = Hematology_Inventory.objects.all()
        return context

@login_required(login_url='/login/')
def chemistry(request):

    return render(request,'inventoryhome/chemistry.html')


class ChemistryListView(SingleTableView):

     model= Chemistry_Inventory
     table_class= ChemistryTable
     template_name= 'inventoryhome/chemistry_inventory.html'


class ChemistryChartView(TemplateView):

    template_name= 'inventoryhome/chemistrychart.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['qs'] = Chemistry_Inventory.objects.all()
        return context



def chemistry_checkout(request):

    if request.method == 'POST':
        form= ChemistryCheckoutForm(request.POST)

        if form.is_valid():

            reagent_name= form.cleaned_data['reagent_name']
            amount_taken= form.cleaned_data['amount_taken']
    # get the reagent object
            reagent = Chemistry_Inventory.objects.get(reagent_name=reagent_name)
    # reduce quantity
            reagent.reagent_quantity -= amount_taken
    # save the object
            reagent.save()
            messages.success(request, '***Reagent Removed From Inventory***')
            if reagent.reagent_quantity <= 0:
                messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')
    form= ChemistryCheckoutForm()
    return render(request,'inventoryhome/chemistry_reagent_checkout.html', {'form' : form})


@login_required(login_url='/login/')
def endo(request):

    return render(request,'inventoryhome/endo.html')


def endo_checkout(request):


    if request.method == 'POST':
        form= EndoCheckoutForm(request.POST)

        if form.is_valid():

            reagent_name= form.cleaned_data['reagent_name']
            amount_taken= form.cleaned_data['amount_taken']
        # get the reagent object
            reagent = Endo_Inventory.objects.get(reagent_name=reagent_name)
        # reduce quantity
            reagent.reagent_quantity -= amount_taken
        # save the object
            reagent.save()
            messages.success(request, '***Reagent Removed From Inventory***')
            if reagent.reagent_quantity <= 0:
                messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')

    form= EndoCheckoutForm()
    return render(request,'inventoryhome/endo_reagent_checkout.html', {'form' : form})

class EndoListView(SingleTableView):

     model= Endo_Inventory
     table_class= EndoTable
     template_name= 'inventoryhome/endo_inventory.html'

class EndoChartView(TemplateView):

    template_name= 'inventoryhome/endochart.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['qs'] = Endo_Inventory.objects.all()
        return context

@login_required(login_url='/login/')
def urines(request):

    return render(request,'inventoryhome/urines.html')

def urines_checkout(request):


    if request.method == 'POST':
        form= UrinesCheckoutForm(request.POST)

        if form.is_valid():

            reagent_name= form.cleaned_data['reagent_name']
            amount_taken= form.cleaned_data['amount_taken']
        # get the reagent object
            reagent = Urines_Inventory.objects.get(reagent_name=reagent_name)
        # reduce quantity
            reagent.reagent_quantity -= amount_taken
        # save the object
            reagent.save()
            messages.success(request, '***Reagent Removed From Inventory***')
            if reagent.reagent_quantity <= 0:
                messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')

    form= UrinesCheckoutForm()
    return render(request,'inventoryhome/urines_reagent_checkout.html', {'form' : form})

class UrinesListView(SingleTableView):

     model= Urines_Inventory
     table_class= UrinesTable
     template_name= 'inventoryhome/urines_inventory.html'

class UrinesChartView(TemplateView):

    template_name= 'inventoryhome/urineschart.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['qs'] = Urines_Inventory.objects.all()
        return context

@login_required(login_url='/login/')
def gasesmetals(request):

    return render(request,'inventoryhome/gasesmetals.html')

def gasesmetals_checkout(request):


    if request.method == 'POST':
        form= GasesMetalsCheckoutForm(request.POST)

        if form.is_valid():

            reagent_name= form.cleaned_data['reagent_name']
            amount_taken= form.cleaned_data['amount_taken']
        # get the reagent object
            reagent = GasesMetals_Inventory.objects.get(reagent_name=reagent_name)
        # reduce quantity
            reagent.reagent_quantity -= amount_taken
        # save the object
            reagent.save()
            messages.success(request, '***Reagent Removed From Inventory***')
            if reagent.reagent_quantity <= 0:
                messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')

    form= GasesMetalsCheckoutForm()
    return render(request,'inventoryhome/gasesmetals_reagent_checkout.html', {'form' : form})

class GasesMetalsListView(SingleTableView):

     model= GasesMetals_Inventory
     table_class= GasesMetalsTable
     template_name= 'inventoryhome/gasesmetals_inventory.html'

class GasesMetalsChartView(TemplateView):

    template_name= 'inventoryhome/gasesmetalschart.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['qs'] = GasesMetals_Inventory.objects.all()
        return context

@login_required(login_url='/login/')
def coagulation(request):

    return render(request,'inventoryhome/coagulation.html')

def coagulation_checkout(request):


    if request.method == 'POST':
        form= CoagulationCheckoutForm(request.POST)

        if form.is_valid():

            reagent_name= form.cleaned_data['reagent_name']
            amount_taken= form.cleaned_data['amount_taken']
        # get the reagent object
            reagent = Coagulation_Inventory.objects.get(reagent_name=reagent_name)
        # reduce quantity
            reagent.reagent_quantity -= amount_taken
        # save the object
            reagent.save()
            messages.success(request, '***Reagent Removed From Inventory***')
            if reagent.reagent_quantity <= 0:
                messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')

    form= CoagulationCheckoutForm()
    return render(request,'inventoryhome/coagulation_reagent_checkout.html', {'form' : form})

class CoagulationListView(SingleTableView):

     model= Coagulation_Inventory
     table_class= CoagulationTable
     template_name= 'inventoryhome/coagulation_inventory.html'

class CoagulationChartView(TemplateView):

    template_name= 'inventoryhome/coagulationchart.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['qs'] = Coagulation_Inventory.objects.all()
        return context

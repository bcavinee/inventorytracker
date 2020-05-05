from django.shortcuts import render
from .models import Hematology_Inventory, Chemistry_Inventory, Endo_Inventory, Coagulation_Inventory, GasesMetals_Inventory, Urines_Inventory
from django.views.generic import ListView, TemplateView
from django_tables2 import SingleTableView
from .tables import HematologyTable, ChemistryTable, EndoTable, CoagulationTable, GasesMetalsTable, UrinesTable
from .forms import HematologyCheckoutForm, ChemistryCheckoutForm, UrinesCheckoutForm, CoagulationCheckoutForm, EndoCheckoutForm, GasesMetalsCheckoutForm, HematologyAverageUseForm, HematologyDownloadAll
from django.db.models import F, Sum, Avg
from django_tables2 import SingleTableView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import datetime
#from datetime import timedelta
from simple_history.models import HistoricalRecords
import xlwt
from django.http import HttpResponse
import itertools

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
            reagent.average_use = amount_taken

        # save the object
            try:
                reagent.save()
                messages.success(request, '***Reagent Removed From Inventory***')


                if reagent.reagent_quantity == 0:
                    messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')

            except IntegrityError:

                messages.success(request, f'***ZERO {reagent} REMAINING NOTIFY SPECALIST***')


            #if reagent.reagent_quantity <= 0:
            #    messages.success(request, f'***{reagent} DEPLETION NOTIFY SPECALIST***')


    #test= Hematology_Inventory.history.filter(history_date__range=["2020-04-29 22:21:19.540507", "2020-04-29 22:22:08.372321"],reagent_name= 'Testing').values('average_use').distinct()
    test= Hematology_Inventory.history.filter(history_date__range=["2020-04-29 22:21:19.540507", "2020-04-29 22:22:08.372321"],reagent_name= 'Testing').aggregate(Sum('average_use'))
    print(test)
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



def hematology_average_use(request):

    if request.method == 'POST':
        form= HematologyAverageUseForm(request.POST)

        if form.is_valid():
            reagent_name= form.cleaned_data['reagent_name']
            start_date= form.cleaned_data['start_date']
            end_date= form.cleaned_data['end_date']
            new_end = end_date + datetime.timedelta(days=1)
            #USED FOR QUERYING ALLreagent_test= Hematology_Inventory.history.values_list('reagent_name')

            reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, new_end],reagent_name= reagent_name).aggregate(Sum('average_use'))

            #reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, end_date],reagent_name= reagent_name).aggregate(Sum('average_use'))
            #reagent= Hematology_Inventory.history.filter(history_date__gte=start_date,history_date__lte=end_date,reagent_name= reagent_name).aggregate(Sum('average_use'))
            #average= Hematology_Inventory.history.filter(history_date__range=[start_date, end_date],reagent_name= reagent_name).aggregate(Avg('average_use'))
            results= reagent['average_use__sum']
            messages.success(request, f'Total Use of {reagent_name} from {start_date} - {end_date} = {results}')

    form= HematologyAverageUseForm()
    return render(request,'inventoryhome/hematologyaverageuse.html', {'form' : form})


def hematology_download_all(request):

    if request.method == 'POST':
        form= HematologyDownloadAll(request.POST)

        if form.is_valid():
            start_date= form.cleaned_data['start_date']
            end_date= form.cleaned_data['end_date']
            new_end = end_date + datetime.timedelta(days=1)

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = f'attachment; filename="HematologyInventory_{start_date}-{end_date} .xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Monthly Reagent Use Report')


            col_width = 256 * 25
            try:
                for i in itertools.count():
                    ws.col(i).width = col_width
            except ValueError:
                pass
                # first_col = ws.col(0)
                # first_col.width = 256 * 100
            ws.write(0,0,'Data From')
            ws.write(1,0,f'{start_date} to {end_date}')
            ws.write(0,1,'Reagesnt Name')
            ws.write(0,2,'Total Monthly Use')

            reagent_test= Hematology_Inventory.history.values_list('reagent_name')

            my_list= []
            for n in reagent_test:
                my_list += n

            my_list = list(set(my_list))

            num=1
            for r in my_list:
                reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, new_end],reagent_name= r).aggregate(Sum('average_use'))
                ws.write(0+num,1,r)
                ws.write(0+num,2,reagent['average_use__sum'])
                num += 1
            wb.save(response)
            return response
    form= HematologyDownloadAll()
    return render(request,'inventoryhome/hematologydownloadall.html', {'form' : form})


#This function has a checkbox to check if you want to download all reagent data to an excel add_sheet
# def hematology_average_use(request):
#
#     if request.method == 'POST':
#         form= HematologyAverageUseForm(request.POST)
#
#         if form.is_valid():
#             reagent_name= form.cleaned_data['reagent_name']
#             start_date= form.cleaned_data['start_date']
#             end_date= form.cleaned_data['end_date']
#             download_all_reagent_data= form.cleaned_data['download_all_reagent_data']
#             new_end = end_date + datetime.timedelta(days=1)
#             if download_all_reagent_data == False:
#             #USED FOR QUERYING ALLreagent_test= Hematology_Inventory.history.values_list('reagent_name')
#
#                 reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, new_end],reagent_name= reagent_name).aggregate(Sum('average_use'))
#
#             #reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, end_date],reagent_name= reagent_name).aggregate(Sum('average_use'))
#             #reagent= Hematology_Inventory.history.filter(history_date__gte=start_date,history_date__lte=end_date,reagent_name= reagent_name).aggregate(Sum('average_use'))
#             #average= Hematology_Inventory.history.filter(history_date__range=[start_date, end_date],reagent_name= reagent_name).aggregate(Avg('average_use'))
#                 results= reagent['average_use__sum']
#                 messages.success(request, f'Total Use of {reagent_name} from {start_date} - {end_date} = {results}')
#             elif download_all_reagent_data == True:
#                 response = HttpResponse(content_type='application/ms-excel')
#                 response['Content-Disposition'] = f'attachment; filename="{start_date}-{end_date}HematologyInventory.xls"'
#
#                 wb = xlwt.Workbook(encoding='utf-8')
#                 ws = wb.add_sheet('Monthly Reagent Use Report')
#
#                 col_width = 256 * 25
#                 try:
#                     for i in itertools.count():
#                         ws.col(i).width = col_width
#                 except ValueError:
#                     pass
#                 # first_col = ws.col(0)
#                 # first_col.width = 256 * 100
#                 ws.write(0,0,'Data From')
#                 ws.write(1,0,f'{start_date} to {end_date}')
#                 ws.write(0,1,'Reagesnt Name')
#                 ws.write(0,2,'Total Monthly Use')
#
#                 reagent_test= Hematology_Inventory.history.values_list('reagent_name')
#                 my_list= []
#                 for n in reagent_test:
#                     my_list += n
#
#                 my_list = list(set(my_list))
#
#                 print(my_list)
#                 num=1
#                 for r in my_list:
#                     reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, end_date],reagent_name= r).aggregate(Sum('average_use'))
#                     ws.write(0+num,1,r)
#                     ws.write(0+num,2,reagent['average_use__sum'])
#                     num += 1
#                     print(reagent)
#                 wb.save(response)
#                 return response
#     form= HematologyAverageUseForm()
#     return render(request,'inventoryhome/hematologyaverageuse.html', {'form' : form})



def log_all():

    reagent_test= Hematology_Inventory.history.values_list('reagent_name')
    my_list= []
    for n in reagent_test:
        my_list += n

    my_list = list(set(my_list))
    for r in my_list:
        reagent= Hematology_Inventory.history.filter(history_date__range=[start_date, new_end],reagent_name= r).aggregate(Sum('average_use'))
        messages.success(request, f'Total Use of {r} from {start_date} - {end_date} = {reagent}')

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Monthly Reagent Use Report')


    ws.write(0,1,'Reagesnt Name')
    ws.write(0,2,'Total Monthly Use')

    reagent_test= Hematology_Inventory.history.values_list('reagent_name')
    my_list= []
    for n in reagent_test:
        my_list += n

    my_list = list(set(my_list))

    print(my_list)
    num=1
    for r in my_list:
        reagent= Hematology_Inventory.history.filter(history_date__range=['2020-04-02', '2020-05-30'],reagent_name= r).aggregate(Sum('average_use'))
        ws.write(0+num,1,r)
        ws.write(0+num,2,reagent['average_use__sum'])
        num += 1
        print(reagent)
    wb.save(response)
    return response

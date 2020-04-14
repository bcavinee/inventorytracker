import django_tables2 as tables
from .models import Hematology_Inventory, Chemistry_Inventory
from django_tables2 import SingleTableView, TemplateColumn



class HematologyTable(tables.Table):
    class Meta:
        model= Hematology_Inventory
        template_name= 'django_tables2/bootstrap.html'
        fields= ('reagent_name','reagent_quantity',)
        #template_name= 'inventoryhome/hematology_inventory.html'


class ChemistryTable(tables.Table):
    class Meta:
        model= Chemistry_Inventory
        template_name= 'django_tables2/bootstrap.html'
        fields= ('reagent_name','reagent_quantity',)
        #template_name= 'inventoryhome/chemistry_inventory.html'




#class HematologyTable(tables.Table):
#    class Meta:
#        model= Hematology_Inventory
        #template_name= 'django_tables2/bootstrap.html'
        #fields= ('reagent name','Reagent quantity',)
#        template_name= 'inventoryhome/hematology_inventory.html'

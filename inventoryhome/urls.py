from django.urls import path
from . import views
from inventoryhome.views import (
HematologyListView, ChemistryListView, GasesMetalsListView, CoagulationListView, UrinesListView, EndoListView,
HematologyChartView, ChemistryChartView, CoagulationChartView, UrinesChartView, GasesMetalsChartView, EndoChartView
)



urlpatterns = [
    path('', views.home, name='inventory-home'),
    path('about/', views.about, name='inventory-about'),
    path('hematology/',views.hematology, name='inventory-hematology'),
    path('hematology_inventory/',views.HematologyListView.as_view(), name='inventory-hematology_inventory'),
    path('hematology_checkout/',views.hematology_checkout, name= 'inventory-hematology_checkout'),
    path('hematology_averageuse/',views.hematology_average_use, name= 'inventory-hematology_average_use'),
    path('coagulation/',views.coagulation, name='inventory-coagulation'),
    path('coagulation_inventory/',views.CoagulationListView.as_view(), name='inventory-coagulation_inventory'),
    path('cogulation_checkout/',views.coagulation_checkout, name= 'inventory-coagulation_checkout'),
    path('urines/',views.urines, name='inventory-urines'),
    path('urines_inventory/',views.UrinesListView.as_view(), name='inventory-urines_inventory'),
    path('urines_checkout/',views.urines_checkout, name= 'inventory-urines_checkout'),
    path('gasesmetals/',views.gasesmetals, name='inventory-gasesmetals'),
    path('gasesmetals_inventory/',views.GasesMetalsListView.as_view(), name='inventory-gasesmetals_inventory'),
    path('gasesmetals_checkout/',views.gasesmetals_checkout, name= 'inventory-gasesmetals_checkout'),
    path('endo/',views.endo, name='inventory-endo'),
    path('endo_inventory/',views.EndoListView.as_view(), name='inventory-endo_inventory'),
    path('endo_checkout/',views.endo_checkout, name= 'inventory-endo_checkout'),
    path('chemistry/',views.chemistry, name='inventory-chemistry'),
    path('chemistry_inventory/',views.ChemistryListView.as_view(), name='inventory-chemistry_inventory'),
    path('chemistry_checkout/',views.chemistry_checkout, name= 'inventory-chemistry_checkout'),
    path('hematology_graph/',views.HematologyChartView.as_view(), name= 'inventory-hematology_graph'),
    path('chemistry_graph/',views.ChemistryChartView.as_view(), name= 'inventory-chemistry_graph'),
    path('urines_graph/',views.UrinesChartView.as_view(), name= 'inventory-urines_graph'),
    path('gasesmetals_graph/',views.GasesMetalsChartView.as_view(), name= 'inventory-gasesmetals_graph'),
    path('coagulation_graph/',views.CoagulationChartView.as_view(), name= 'inventory-coagulation_graph'),
    path('endo_graph/',views.EndoChartView.as_view(), name= 'inventory-endo_graph'),
    #THIS WAS A TEST PATH FOR EXPORTING TO Excel
    #path(r'exportexcel', views.export_users_xls, name='inventory-export_users_xls'),
    path('hematology_download_all/',views.hematology_download_all, name= 'inventory-hematology_download_all'),

]



#path('masterlist/', views.master_inventory_list, name='inventory-masterlist')

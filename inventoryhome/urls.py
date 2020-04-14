from django.urls import path
from . import views
from inventoryhome.views import HematologyListView, ChemistryListView, HematologyChartView, ChemistryChartView


urlpatterns = [
    path('', views.home, name='inventory-home'),
    path('about/', views.about, name='inventory-about'),
    path('hematology/',views.hematology, name='inventory-hematology'),
    path('hematology_inventory/',views.HematologyListView.as_view(), name='inventory-hematology_inventory'),
    path('hematology_checkout/',views.hematology_checkout, name= 'inventory-hematology_checkout'),
    path('chemistry/',views.chemistry, name='inventory-chemistry'),
    path('chemistry_inventory/',views.ChemistryListView.as_view(), name='inventory-chemistry_inventory'),
    path('chemistry_checkout/',views.chemistry_checkout, name= 'inventory-chemistry_checkout'),
    path('hematology_graph/',views.HematologyChartView.as_view(), name= 'inventory-hematology_graph'),
    path('chemistry_graph/',views.ChemistryChartView.as_view(), name= 'inventory-chemistry_graph'),

]



#path('masterlist/', views.master_inventory_list, name='inventory-masterlist')

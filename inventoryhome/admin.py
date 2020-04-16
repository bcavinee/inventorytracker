from django.contrib import admin
from .models import Hematology_Inventory, Chemistry_Inventory, Endo_Inventory, Coagulation_Inventory, GasesMetals_Inventory, Urines_Inventory
# Register your models here.


admin.site.register(Hematology_Inventory)
admin.site.register(Chemistry_Inventory)
admin.site.register(Urines_Inventory)
admin.site.register(GasesMetals_Inventory)
admin.site.register(Coagulation_Inventory)
admin.site.register(Endo_Inventory)

from django.contrib import admin
from .models import Hematology_Inventory, Chemistry_Inventory, Endo_Inventory, Coagulation_Inventory, GasesMetals_Inventory, Urines_Inventory
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.site_header= 'Inventory Adminstration Dashboard'

class Hematology_InventoryAdmin(admin.ModelAdmin):
    exclude = ('average_use',)

admin.site.register(Hematology_Inventory,Hematology_InventoryAdmin)
#admin.site.register(Hematology_Inventory,SimpleHistoryAdmin)
admin.site.register(Chemistry_Inventory)
admin.site.register(Urines_Inventory)
admin.site.register(GasesMetals_Inventory)
admin.site.register(Coagulation_Inventory)
admin.site.register(Endo_Inventory)

from django.contrib import admin
from cars.models import carro 
from cars.models import marca
from cars import models as md

class carro_admin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'marca', 'ano_fabricacao', 'ano_modelo', 'placa', 'carro_foto', 'valor')
    search_fields = ('modelo',)


    

class marca_admin(admin.ModelAdmin):
    list_display = ('id', 'marca_nome',)
    search_fields = ('marca_nome',)



class car_inventoryAdmin(admin.ModelAdmin):
    list_display = ('car_count', 'car_value', 'car_date')
    search_fields = ('car_date',)


admin.site.register(marca, marca_admin)
admin.site.register(carro, carro_admin)
admin.site.register(md.car_inventory, car_inventoryAdmin)




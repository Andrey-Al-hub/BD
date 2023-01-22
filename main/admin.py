from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'amount', 
                'expiration_date', 'manufacturer')

    list_display_links = ('title',)

    search_fields = ('title', 'category')

    list_filter = ('manufacturer', 'price')


admin.site.register(Product, ProductAdmin)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'city')

    list_display_links = ('manufacturer',)

@admin.register(Operation_on_product)
class Operation_on_productAdmin(admin.ModelAdmin):
    pass

@admin.register(Operation_type)
class Operation_typeAdmin(admin.ModelAdmin):
    list_display = ('operation_type', 'percent',)

    list_display_links = ('operation_type',)
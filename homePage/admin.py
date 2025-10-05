from django.contrib import admin
from .models import Products,Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active',)
    list_filter = ('active', 'name',) 
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name','quantity', 'amount', 'paid',)
    list_filter = ('paid', 'product_name',) 
    search_fields = ('user', 'product_name',)


admin.site.register(Products, ProductAdmin)
admin.site.register(Order, OrderAdmin)

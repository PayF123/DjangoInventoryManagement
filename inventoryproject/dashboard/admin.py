from django.contrib import admin

from .models import Product, Assembly, Component,Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Assembly)
admin.site.register(Component)
admin.site.register(Order)
# admin.site.register(Warehouse)
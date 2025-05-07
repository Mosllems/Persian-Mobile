from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'category',]

admin.site.register(Product, ProductAdmin)
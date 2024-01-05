from django.contrib import admin
from .models import CategoryModule, ProductModule

class CategoryDetails(admin.ModelAdmin):
    list_display = ['id', 'name']

class ProductDetails(admin.ModelAdmin):
    list_display = ['id','category', 'title', 'pCategory', 'price', 'brand']

# Register your models here.
admin.site.register(CategoryModule, CategoryDetails)
admin.site.register(ProductModule, ProductDetails)
from django.contrib import admin
from .models import Category, Product
from .models import Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name', 'description']



admin.site.register(Contact)
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'is_available', 'created_at', 'created_by')
    list_filter = ('categories', 'is_available', 'created_by')
    fieldsets = (
        (None, { 'fields': ['name', 'created_by', 'created_at']}),
        ('Availability', { 'fields': ['is_available', 'stock_quantity']}),
        ('Categories', { 'fields': ['categories']}),
        ('Other Details', { 'fields': ['price','image','description'], 'classes': ('collapse',)}),
        )
    readonly_fields = ('created_at',)
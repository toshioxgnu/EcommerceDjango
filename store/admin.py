from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_stock','category', 'created_date','modified_date','is_available')
    prepolated_fields = {'slug' : ('product_name',)}



admin.site.register(Product)

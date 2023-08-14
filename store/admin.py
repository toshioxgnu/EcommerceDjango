from django.contrib import admin
from .models import Product, Variation

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_stock','category', 'created_date','modified_date','is_available')
    prepolated_fields = {'slug' : ('product_name',)}
    list_editable = ('is_available',)
    list_filter = ('product_name', 'product_price', 'product_stock','category', 'created_date','modified_date','is_available')

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value','variation_price', 'created_date','modified_date','is_active')
    list_editable = ('is_active',)
    prepolated_fields = {'variation_price' : ('0',)}
    list_filter = ('product', 'variation_category', 'variation_value','variation_price', 'created_date','modified_date','is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)

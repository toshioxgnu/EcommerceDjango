from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_stock = models.IntegerField()
    product_image_url = models.ImageField( upload_to='photos/products' )
    product_description = models.TextField( max_length=500, blank=True )
    product_slug = models.SlugField(max_length=200, unique=True)
    is_available=models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ) 
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now_add=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.product_slug])

    def __str__(self):
        return self.product_name
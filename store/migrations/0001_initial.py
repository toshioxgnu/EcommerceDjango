# Generated by Django 4.2.1 on 2023-06-07 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.FloatField()),
                ('product_stock', models.IntegerField()),
                ('product_image_url', models.ImageField(upload_to='photos/products')),
                ('product_description', models.TextField(blank=True, max_length=500)),
                ('product_slug', models.SlugField(max_length=200, unique=True)),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]

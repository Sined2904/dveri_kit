# Generated by Django 4.2.8 on 2024-06-18 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_remove_product_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productalbum',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_product', to='products.product', verbose_name='Дверь'),
        ),
    ]

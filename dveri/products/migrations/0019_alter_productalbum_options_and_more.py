# Generated by Django 4.2.8 on 2024-01-24 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_product_color_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productalbum',
            options={'ordering': ('-time_create', 'name'), 'verbose_name': 'Фотографии товара', 'verbose_name_plural': 'Фотографии товаров'},
        ),
        migrations.AlterModelOptions(
            name='productalbumcolor',
            options={'ordering': ('-time_create', 'name'), 'verbose_name': 'Фотографии расцветок товара', 'verbose_name_plural': 'Фотографии расцветок товаров'},
        ),
        migrations.AddField(
            model_name='productalbum',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productalbumcolor',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]

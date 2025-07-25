# Generated by Django 4.2.8 on 2023-12-08 17:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('entrance_door', 'Входная дверь'), ('interior_door', 'Межкомнатная дверь'), ('window', 'Окно'), ('roller_shutters', 'Рольставни')], default=None, max_length=50, verbose_name='Выберите тип товара')),
                ('category', models.CharField(choices=[('royal', 'Царговые'), ('pvc', 'ПВХ'), ('veneer', 'Шпон'), ('laminate', 'Ламинат'), ('solid', 'Массив натуральный')], default=None, max_length=50, verbose_name='Выберите тип двери (для межкомнатных дверей)')),
                ('name', models.CharField(max_length=250, verbose_name='Название товара')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена товара')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SizeDoor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=256, verbose_name='Размер двери')),
            ],
            options={
                'verbose_name': 'Размер двери',
                'verbose_name_plural': 'Размеры дверей',
                'ordering': ('size',),
            },
        ),
        migrations.CreateModel(
            name='RelatedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название сопутствующего товара')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена сопутствующего товара')),
                ('image', models.ImageField(blank=True, null=True, upload_to='related_product/', verbose_name='Фото сопутствующего товара')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание сопутствующего товара')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='products.product', verbose_name='Дверь')),
            ],
            options={
                'verbose_name': 'Сопутствующий товар',
                'verbose_name_plural': 'Сопутствующие товары',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, related_name='door', to='products.sizedoor', verbose_name='Размеры двери'),
        ),
        migrations.CreateModel(
            name='DoorAlbumColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название цвета')),
                ('image', models.ImageField(upload_to='doors_color/', verbose_name='Фото')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_color', to='products.product', verbose_name='Дверь')),
            ],
            options={
                'verbose_name': 'Фотографии цветов двери',
                'verbose_name_plural': 'Фотографии цветов двери',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DoorAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название фото')),
                ('image', models.ImageField(upload_to='doors/', verbose_name='Фото')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_door', to='products.product', verbose_name='Дверь')),
            ],
            options={
                'verbose_name': 'Фотографии двери',
                'verbose_name_plural': 'Фотографии двери',
                'ordering': ('name',),
            },
        ),
    ]

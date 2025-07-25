# Generated by Django 4.2.8 on 2023-12-18 21:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_for_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок статьи')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание товара')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]

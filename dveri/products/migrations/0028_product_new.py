# Generated by Django 4.2.8 on 2024-06-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_productalbum_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False, verbose_name='Новинка'),
            preserve_default=False,
        ),
    ]

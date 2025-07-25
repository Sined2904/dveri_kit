# Generated by Django 4.2.8 on 2023-12-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_requestformeasurement_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForCallback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия Имя')),
                ('telefone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заявка на обратный звонок',
                'verbose_name_plural': 'Заявки на обратный звонок',
                'ordering': ['-time_create'],
            },
        ),
    ]

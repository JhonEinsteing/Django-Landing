# Generated by Django 2.2.12 on 2020-05-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0013_auto_20200528_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='NombDocu',
            field=models.CharField(max_length=255, verbose_name='Nombre del documento'),
        ),
    ]

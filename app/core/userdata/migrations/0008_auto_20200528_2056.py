# Generated by Django 2.2.12 on 2020-05-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0007_auto_20200528_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Perfil de Usuario', 'verbose_name_plural': 'Perfiles de Usuario'},
        ),
        migrations.AlterField(
            model_name='roles',
            name='RoleName',
            field=models.CharField(max_length=50, verbose_name='Roles'),
        ),
    ]

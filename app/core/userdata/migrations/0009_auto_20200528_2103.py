# Generated by Django 2.2.12 on 2020-05-29 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0008_auto_20200528_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='RoleName',
            field=models.CharField(max_length=50, null=True, verbose_name='Roles'),
        ),
    ]

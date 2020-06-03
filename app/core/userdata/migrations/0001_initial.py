# Generated by Django 2.2.12 on 2020-05-09 04:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userDNI', models.CharField(max_length=20)),
                ('fotoUser', models.ImageField(default='user.png', upload_to='', verbose_name='Foto de perfil')),
                ('teleUser', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HabilUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombHabil', models.CharField(max_length=100)),
                ('DescHabilidad', ckeditor.fields.RichTextField(max_length=2000, verbose_name='Descripcion de la Habilidad')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcrHabil', models.DecimalField(decimal_places=1, max_digits=2)),
                ('udtHabil', models.DateField(auto_now=True)),
                ('idHabil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.HabilUser')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser')),
            ],
        ),
        migrations.CreateModel(
            name='DetaRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addUser', models.DateTimeField(auto_now_add=True)),
                ('udtuser', models.DateTimeField(auto_now=True)),
                ('estaRol', models.CharField(max_length=10)),
                ('idRol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.Roles', verbose_name='Identificador de Rol')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser')),
            ],
        ),
    ]

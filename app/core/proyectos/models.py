from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import DatosUser
# Create your models here.

class TipoDocu(models.Model):
    NombToDoc = models.CharField(max_length=50, verbose_name="Nombre de tipo de documento")

    class Meta:
        verbose_name = "Tipo de Documento"

        verbose_name_plural = "Documento"

    def __str__(self):
        return self.NombToDoc
 
class CategProye(models.Model):
    tipoproy = models.CharField(max_length=100, null=True, verbose_name="Tipo de proyecto")
    Languaje = models.CharField(max_length=45, null=True, verbose_name="Languaje de programación")
    MotorDB = models.CharField(max_length=155, null=True, verbose_name="Base de datos usada")
    Arquitectura = models.CharField(max_length=255, verbose_name="Arquitectura")

    class Meta:
        verbose_name = "Tipo de Categoria"

        verbose_name_plural = "Categoria"

    def __str__(self):
        return self.tipoproy


class Proyectos(models.Model):
    idCategProye = models.ForeignKey(CategProye, null=True, on_delete = models.CASCADE, verbose_name ="Identificador de CategProye") 
    NombProy = models.CharField(max_length=255, verbose_name="Nombre del proyecto")
    DescProy = models.TextField(verbose_name = "Descripcion de proyecto", null=True)
    imgProy = models.ImageField(upload_to="img/proyectos", null=True, verbose_name = "Foto del proyecto")
    FechaIni = models.DateField(auto_now_add = False, auto_now=False, null=True, verbose_name="Fecha de Inicio")
    FechaFin = models.DateField(auto_now_add = False, auto_now=False, null=True, verbose_name="Fecha de Finalización")
    UrlRepo = models.TextField(verbose_name = "Direccion URL del proyecto", null=True)

    class Meta:
        verbose_name = "Total Proyectos"

        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.NombProy


class Documentos(models.Model):
    idtipoDocu = models.ForeignKey(TipoDocu, on_delete = models.CASCADE, verbose_name ="Identificador de Tipodocu")
    idUsuarios = models.ForeignKey(DatosUser, default=1, on_delete = models.CASCADE, verbose_name ="Identificador de DatosUser")
    idProyectos = models.ForeignKey(Proyectos,default=1, on_delete = models.CASCADE, verbose_name ="Identificador de Proyectos")
    NombDocu = models.CharField(max_length=255, verbose_name="Nombre del documento")
    documento = models.FileField(upload_to = "documentos/proyectos", null=True, verbose_name="Archivo")

    class Meta:
        verbose_name = "Documentacion de Proyecto"

        verbose_name_plural = "Documentos de Proyecto"

    def __str__(self):
        return self.NombDocu


 
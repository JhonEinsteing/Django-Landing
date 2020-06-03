from django.contrib import admin

# Register your models here.
from.models import TipoDocu, CategProye, Proyectos, Documentos

class TipoDocuModel(admin.ModelAdmin):
    list_display = ["NombToDoc"]
    list_display_links = ["NombToDoc"]
    list_filter = ["NombToDoc"]
    
    class Meta:
        model: TipoDocu

admin.site.register(TipoDocu)


class CategProyeModel(admin.ModelAdmin):
    list_display = ["Arquitectura"]

    class Meta:
        model: CategProye
        
admin.site.register(CategProye)

class ProyectosModel(admin.ModelAdmin):
    list_display = ["NombProy"]

    class Meta:
        model:Proyectos

admin.site.register(Proyectos)

class DocumentosModel(admin.ModelAdmin):
    list_display = ["NombDocu"]

    class Meta:
        model:Documentos

admin.site.register(Documentos)

from tabnanny import verbose
from django.db import models

class Curso(models.Model):
    id = models.AutoField(primary_key=True)#id auto_increment
    nombre= models.CharField(max_length=255,verbose_name="Nombre")#campo de texto
    descripcion= models.TextField(null=False,verbose_name="Descripcion")

    def __str__(self):
        fila= "Nombre "+self.nombre+"-"+" Descripcion "+self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

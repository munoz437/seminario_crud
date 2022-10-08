from tabnanny import verbose
from django.db import models
from docente.models import Docente

class Curso(models.Model):
    id = models.AutoField(primary_key=True)#id auto_increment
    nombre= models.CharField(max_length=255,verbose_name="Nombre")#campo de texto
    descripcion= models.TextField(null=False,verbose_name="Descripcion")
    creditos= models.PositiveSmallIntegerField(null=True,verbose_name="Creditos")
    docente= models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Docente")

    def __str__(self):
        fila= "Nombre "+self.nombre+"-"+" Descripcion "+self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

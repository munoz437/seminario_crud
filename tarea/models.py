from tabnanny import verbose
from tkinter import Widget
from django.db import models

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)#id auto_increment
    titulo= models.CharField(max_length=255,verbose_name="Titulo")#campo de texto
    descripcion= models.TextField(null=False,verbose_name="Descripcion")
    punteo= models.IntegerField(null=False,verbose_name="Punteo")
    fechaVencimiento= models.CharField(max_length=255,null=False,verbose_name="Fecha de Vencimiento")

    def __str__(self):
        fila= "Titulo "+self.titulo+"-"+" Descripcion "+self.descripcion+" "+self.punteo+" "+self.fechaVencimiento
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()
    class Meta:
        verbose_name='Tarea'
        verbose_name_plural='Tareas'
        db_table='tbl_tareas'
        ordering=['id']
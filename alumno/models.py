from tabnanny import verbose
from django.db import models

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)#id auto_increment
    nombres= models.CharField(max_length=255,verbose_name="Nombres")#campo de texto
    apellidos= models.TextField(null=False,verbose_name="Apellidos")

    def __str__(self):
        fila= "Nombres "+self.nombres+"-"+" Apellidos "+self.apellidos
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

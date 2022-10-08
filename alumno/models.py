from tabnanny import verbose
from django.db import models

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)#id auto_increment
    nombres= models.CharField(max_length=255,verbose_name="Nombres")#campo de texto
    apellidos= models.TextField(null=False,verbose_name="Apellidos")

    def __str__(self):
        fila= self.nombres+" "+self.apellidos
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()
    class Meta:
        verbose_name='Alumno'
        verbose_name_plural='Alumnos'
        db_table='tbl_alumnos'
        ordering=['apellidos','-nombres']
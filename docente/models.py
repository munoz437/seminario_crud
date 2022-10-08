from tabnanny import verbose
from django.db import models

class Docente(models.Model):
    id = models.AutoField(primary_key=True)#id auto_increment
    nombres= models.CharField(max_length=255,verbose_name="Nombres")#campo de texto
    apellidos= models.TextField(null=False,verbose_name="Apellidos")
    fecha_nacimiento=models.DateField(null=True,verbose_name="Fecha nacimiento")


    def __str__(self):
        fila= self.nombres+" "+self.apellidos
        return fila

    def delete(self, using=None, keep_parents=False):
        super().delete()

    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'
        db_table='tbl_docentes'
        ordering=['apellidos','-nombres']

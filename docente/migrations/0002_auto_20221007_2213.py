# Generated by Django 3.0.5 on 2022-10-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docente',
            options={'ordering': ['apellidos', '-nombres'], 'verbose_name': 'Docente', 'verbose_name_plural': 'Docentes'},
        ),
        migrations.AddField(
            model_name='docente',
            name='fecha_nacimiento',
            field=models.DateField(null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterModelTable(
            name='docente',
            table='tbl_docentes',
        ),
    ]

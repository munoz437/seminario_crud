# Generated by Django 3.0.5 on 2022-10-08 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0007_auto_20221001_2319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarea',
            options={'ordering': ['id'], 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.AlterModelTable(
            name='tarea',
            table='tbl_tareas',
        ),
    ]

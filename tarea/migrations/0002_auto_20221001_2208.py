# Generated by Django 3.0.5 on 2022-10-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechaVencimiento',
            field=models.CharField(max_length=255, verbose_name='Fecha de Vencimiento'),
        ),
    ]
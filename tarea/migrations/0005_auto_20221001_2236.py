# Generated by Django 3.0.5 on 2022-10-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0004_auto_20221001_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechaVencimiento',
            field=models.DateTimeField(max_length=255, verbose_name='Fecha de Vencimiento'),
        ),
    ]
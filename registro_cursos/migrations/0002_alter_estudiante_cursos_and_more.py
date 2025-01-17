# Generated by Django 4.2 on 2024-05-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='cursos',
            field=models.ManyToManyField(related_name='estudiantes', to='registro_cursos.curso'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='modificacion_registro',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 2.2.9 on 2021-01-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_auto_20201230_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='a',
            field=models.IntegerField(choices=[(0, 'LUNES'), (1, 'MARTES'), (2, 'MIERCOLES'), (3, 'JUEVES'), (4, 'VIERNES'), (5, 'SABADO'), (6, 'DOMINGO')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='de',
            field=models.IntegerField(choices=[(0, 'LUNES'), (1, 'MARTES'), (2, 'MIERCOLES'), (3, 'JUEVES'), (4, 'VIERNES'), (5, 'SABADO'), (6, 'DOMINGO')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='modalidad',
            field=models.IntegerField(choices=[(0, 'CURSO'), (1, 'TALLER'), (2, 'SEMINARIO'), (3, 'DIPLOMADO'), (4, 'CAPACITACION'), (5, 'CONVERSATORIO')]),
        ),
    ]

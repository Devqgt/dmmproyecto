# Generated by Django 2.2.9 on 2021-02-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='integrantes',
            field=models.ManyToManyField(related_name='persona_servicio', to='inicio.Persona'),
        ),
    ]

# Generated by Django 2.2.9 on 2021-02-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfabetizacion', '0002_auto_20210215_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mujeresalfa',
            name='integrantes',
            field=models.ManyToManyField(related_name='persona_alfabetizacion', to='inicio.Persona'),
        ),
    ]

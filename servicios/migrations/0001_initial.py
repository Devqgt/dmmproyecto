from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.IntegerField(choices=[(0, 'CURSO'), (1, 'TALLER'), (2, 'SEMINARIO'), (3, 'DIPLOMADO'), (4, 'CAPACITACION'), (5, 'CONVERSATORIO')])),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('de', models.IntegerField(choices=[(0, 'LUNES'), (1, 'MARTES'), (2, 'MIERCOLES'), (3, 'JUEVES'), (4, 'VIERNES'), (5, 'SABADO'), (6, 'DOMINGO')])),
                ('a', models.IntegerField(choices=[(0, 'LUNES'), (1, 'MARTES'), (2, 'MIERCOLES'), (3, 'JUEVES'), (4, 'VIERNES'), (5, 'SABADO'), (6, 'DOMINGO')])),
                ('integrantes', models.ManyToManyField(blank=True, to='inicio.Persona')),
            ],
        ),
    ]

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inicio', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunidad', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Agregar Comunidades',
                'verbose_name_plural': 'Agregar Comunidades',
            },
        ),
        migrations.CreateModel(
            name='MujeresAlfa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alfabetizadora', models.CharField(max_length=20)),
                ('ciclo', models.DateField()),
                ('fase', models.IntegerField(choices=[(0, 'FASE INCIAL'), (1, 'PRIMERA DE POST'), (2, 'SEGUNDA DE POST')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alfabetizacion.Comunidad', verbose_name='comunidades')),
                ('integrantes', models.ManyToManyField(to='inicio.Persona')),
            ],
            options={
                'verbose_name': 'Grupos de alfabetizacion',
                'verbose_name_plural': 'Grupos de alfabetizacion',
            },
        ),
    ]

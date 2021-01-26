
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.IntegerField(choices=[(0, 'SAN MARCOS')], default=0)),
                ('municipio', models.IntegerField(choices=[(0, 'SAN PEDRO')], default=0)),
                ('identificador', models.IntegerField(choices=[(0, 'AREA RURAL'), (1, 'AREA URBANA'), (2, 'LLANO GRANDE')])),
                ('zona', models.IntegerField(blank=True, choices=[(0, ''), (1, 'ZONA 1'), (2, 'ZONA 1 Y 2'), (3, 'ZONA 1 Y 4'), (4, 'ZONA 2'), (5, 'ZONA 4'), (6, 'ZONA 3 Y 4')], default=0)),
                ('caserio', models.IntegerField(blank=True, choices=[(0, ''), (1, 'LOS JAZMINES'), (2, 'LLANO GRANDE')], default=0)),
                ('canton', models.IntegerField(blank=True, choices=[(0, ''), (1, 'LA PARROQUIA'), (2, 'SANTA MARIA DE ATOCHA'), (3, 'SAN MIGUEL'), (4, 'SAN JUAN DE DIOS'), (5, 'SAN JUAN DEL POZO'), (6, 'SAN AGUSTÍN TONALÁ'), (7, 'EL MOSQUITO'), (8, 'SAN SEBASTIÁN')], default=0)),
                ('sector', models.IntegerField(blank=True, choices=[(0, ''), (1, 'HIERBA BUENA'), (2, 'GALLO ROJO')], default=0)),
                ('aldeas', models.IntegerField(blank=True, choices=[(0, ''), (1, 'CANTEL'), (2, 'CORRAL GRANDE'), (3, 'CHAMPOLLAP'), (4, 'CHIM'), (5, 'EL CEDRO'), (6, 'EL TABLERO'), (7, 'LA GRANDEZA'), (8, 'MÁVIL'), (9, 'PIEDRA GRANDE'), (10, 'PROVINCIA CHIQUITA'), (11, 'SACUCHÚM'), (12, 'SAN ANDRÉS CHÁPIL'), (13, 'SAN ISIDRO CHAMAC'), (14, 'SAN JOSÉ CÁBEN'), (15, 'SAN PEDRO PETZ'), (16, 'SANTA TERESA'), (17, 'SAN FRANCISCO SOCHE')], default=0)),
                ('paraje', models.CharField(blank=True, max_length=20)),
                ('nombre_grupo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Asiganacion de grupos',
                'verbose_name_plural': 'Asiganacion de grupos',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cui', models.CharField(max_length=20)),
                ('sexo', models.IntegerField(choices=[(0, ''), (1, 'M'), (2, 'F')], default=0)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(blank=True, max_length=20)),
                ('tercer_nombre', models.CharField(blank=True, max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(blank=True, max_length=20)),
                ('apellido_casada', models.CharField(blank=True, max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(blank=True, max_length=8)),
                ('direccion', models.CharField(blank=True, max_length=20)),
                ('correo_electronico', models.EmailField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Registro de personas',
                'verbose_name_plural': 'Registro de personas',
            },
        ),
        migrations.CreateModel(
            name='AsignacionPersonaGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.IntegerField(choices=[(0, 'MIEMBRO'), (1, 'PRESIDENTE'), (2, 'VICE-PRESIDENTE'), (3, 'SECRETARIA'), (4, 'TESORERA'), (5, 'VOCAL 1'), (6, 'VOCAL 2')], default=6)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_directiva', to='inicio.Grupo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_directiva', to='inicio.Persona')),
            ],
            options={
                'verbose_name': 'Asignar Directiva',
                'verbose_name_plural': 'Asignar Directiva',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rol', models.PositiveSmallIntegerField(choices=[(0, 'Administrador'), (1, 'Trabajador Social'), (2, 'Tecnico Capacitador'), (3, 'Promotor de grupos sociales'), (5, 'Secretaria')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

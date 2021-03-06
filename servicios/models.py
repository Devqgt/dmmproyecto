from django.db import models
from inicio.models import *

class Curso(models.Model):
    MODALIDAD = [
        (0, "CURSO"),
        (1, "TALLER"),
        (2, "SEMINARIO"),
        (3, "DIPLOMADO"),
        (4, "CAPACITACION"),
        (5, "CONVERSATORIO"),
    ]
    modalidad = models.IntegerField(choices=MODALIDAD, null=False, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    fecha_inicio = models.DateField(blank= True, null=True)
    fecha_finalizacion = models.DateField(blank= True, null=True)
    hora_inicio = models.TimeField(auto_now=False)
    hora_final = models.TimeField(auto_now=False)
    integrantes = models.ManyToManyField(Persona, related_name="persona_servicio")
    DIAS = [
        (0, "LUNES"),
        (1, "MARTES"),
        (2, "MIERCOLES"),
        (3, "JUEVES"),
        (4, "VIERNES"),
        (5, "SABADO"),
        (6, "DOMINGO")
    ]
    de = models.IntegerField(choices=DIAS, null=False, blank=False)
    a = models.IntegerField(choices=DIAS, null=False, blank=False)
    def __str__(self):
        txt="{0}"
        return txt.format(self.nombre)

    def horario(self):
        txt="De: {0} a: {1}"
        return txt.format(self.de, self.a)
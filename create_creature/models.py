from django.db import models


class Estadisticas(models.Model):
    ataque = models.IntegerField()
    defensa = models.IntegerField()
    velocidad = models.IntegerField()


class Criatura(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    habilidad_especial = models.CharField(max_length=50)
    estadisticas = models.OneToOneField(Estadisticas, on_delete=models.CASCADE)

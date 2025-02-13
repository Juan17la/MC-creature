from django.db import models
from random import randint, choice

class Stats(models.Model): #------> LO HIZE BIEN :) SOLO NOMBRES INCORRECTOS
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    resistance = models.IntegerField()

    @classmethod
    def create_random_stats(cls):
        return cls.objects.create(
            attack=randint(1, 10),
            defense=randint(1, 10),
            speed=randint(1, 10),
            hp=randint(1, 10),
            resistance=randint(1, 10),
        )

class Race(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def select_random_type(cls):
        races = cls.objects.all()
        return choice(races) if races.exists() else None

class SpecialAbility(models.Model): #----> NO HIZE BIEN LA ESTRUCTURA
    name = models.CharField(max_length=50)
    level_power = models.IntegerField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="abilities")

    @classmethod
    def select_random_ability(cls, race):
        habilities = cls.objects.filter(race=race)
        return choice(habilities) if habilities.exists() else None

class Creature(models.Model):
    name = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    special_ability = models.ForeignKey(SpecialAbility, on_delete=models.CASCADE)
    stats = models.ForeignKey(Stats, on_delete=models.CASCADE)

    @classmethod
    def generateCreature(cls, name):
        race_selected = Race.select_random_type()  # Ahora es una instancia de Race
        if not race_selected:  # Verifica que haya razas en la BD
            raise ValueError("No hay razas disponibles en la base de datos")

        newCreature = cls(
            name=name, 
            race=race_selected,  # Ahora es una instancia correcta
            special_ability=SpecialAbility.select_random_ability(race_selected),
            stats=Stats.create_random_stats(),
        )
        newCreature.save()
        return newCreature
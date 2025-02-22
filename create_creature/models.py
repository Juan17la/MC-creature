from django.db import models
from django.contrib.auth.models import User
from random import randint, choice

class Collection(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Un usuario solo tiene una colección
    creatures = models.ManyToManyField("Creature", blank=True)  # Relación con criaturas

    def add_creature(self, creature):
        self.creatures.add(creature)

    def remove_creature(self, creature):
        self.creatures.remove(creature)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def generateCreature(cls, name):
        race_selected = Race.select_random_type()
        if not race_selected:
            raise ValueError("No hay razas disponibles en la base de datos")

        ability = SpecialAbility.select_random_ability(race_selected)
        if not ability:
            ability = SpecialAbility.objects.create(name="Default Ability", level_power=1, race=race_selected)  # Habilidad por defecto

        newCreature = cls.objects.create(
            name=name, 
            race=race_selected,
            special_ability=ability,
            stats=Stats.create_random_stats(),
        )
        return newCreature

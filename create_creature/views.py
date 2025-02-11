from django.shortcuts import render, redirect, HttpResponse
from .forms import NameFormCreature
from .models import Criatura, Estadisticas
from random import choice, randint

def peru(request):
    return HttpResponse('<h1>Perukistan</h1>')

def home(request):
    return render(request, 'home.html', {
        'title': 'Home',
        'rHome' : 'home'
    })


def generate(request):
    if request.method == 'POST':
        form = NameFormCreature(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']

            estadisticas = Estadisticas.objects.create(
                ataque=randint(1, 10),
                defensa=randint(1, 10),
                velocidad=randint(1, 10),
            )

            # Generar tipo y habilidad especial aleatoria
            tipo = choice(['Zombie', 'Humano', 'Esqueleto', 'Enderman', 'Pig'])
            habilidad_especial = choice(['Invisibilidad', 'Fuerza Extrema', 'Velocidad Luz'])

            # Crear la criatura
            criatura = Criatura.objects.create(
                nombre=nombre,
                tipo=tipo,
                habilidad_especial=habilidad_especial,
                estadisticas=estadisticas,
            )

            # Pasar los datos a una página para mostrar la criatura
            return render(request, 'creature_created.html', {
                'title': 'Creature Created',
                'creature': criatura,
            })
    else:
        form = NameFormCreature()

    return render(request, 'generate.html', {
        'form': form,
        'title': 'Generate',
    })

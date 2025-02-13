from django.shortcuts import render, HttpResponse
from .forms import NameFormCreature
from .models import Creature
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
            name = form.cleaned_data['name']

            newCreature = Creature.generateCreature(name)

        return render(request, 'creature_created.html', {
            'title': 'Creature Created',
            'creature': newCreature,})
    else:
        form = NameFormCreature() 
        return render(request, 'generate.html', {
            'form': form,
            'title': 'Generate',})

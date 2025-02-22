from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import createCreature
from .models import Creature, Collection

def home(request):
    return render(request, 'home.html', {
        'title': 'Home',
        'rHome' : 'home'
    })

def collections(request):
    user_collection = None
    if request.user.is_authenticated:
        user_collection, created = Collection.objects.get_or_create(user=request.user)

    return render(request, 'collection.html', {
        'collection': user_collection,
    })

def generate(request):
    if request.method == 'POST':
        form = createCreature(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            newCreature = Creature.generateCreature(name)

            if request.user.is_authenticated:
                collection, created = Collection.objects.get_or_create(user=request.user)
                collection.add_creature(newCreature)
                newCreature.user = request.user
                newCreature.save()

            return render(request, 'creature_created.html', {
                'title': 'Creature Created',
                'creature': newCreature,
            })
    
    else:
        form = createCreature() 
        return render(request, 'generate.html', 
                    {'form': form, 
                    'title': 'Generate'})

def singUp(request):
    if request.method == 'GET':
        return render(request, 'sing_up.html', {
            'registerForm': UserCreationForm,
        })

    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('collection')
            except IntegrityError:
                return render(request, 'sing_up.html', {
                    'registerForm': UserCreationForm,
                    'error' : 'User already exist!' 
                })
        return render(request, 'sing_up.html', {
            'registerForm': UserCreationForm,
            'error' : 'Passwords do not match!'
        })

def singout(request):
    logout(request)
    return redirect('home')

def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
        'formAuth': AuthenticationForm
    })
    else:
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
                'error': 'This user do not exist!'
            })
        else:
            login(request, user)
            return redirect('collection')



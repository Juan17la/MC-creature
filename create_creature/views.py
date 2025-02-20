from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import NameFormCreature
from .models import Creature

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


def collections(request):
    return render(request, 'collection.html')

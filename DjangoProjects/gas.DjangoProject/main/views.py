from django.shortcuts import render
from .models import Worker, BaseOfOil, Clients

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def database(request):
    data = {
        'worker' : Worker.objects.all(),
        'bases': BaseOfOil.objects.all(),
        'clients' : Clients.objects.all()
    }
    return render(request, 'main/database.html' , {'data' : data})

def komanda(request):
    data = {
        'director': {
            'name': 'Дюсембеев Дильдар',
            'mail' : 'dildar@mail.ru',
            'tel': '+7 707 747 77 77',
            'city': 'Almaty'

        }
    }
    return render(request, 'main/komanda.html', data)


from django.shortcuts import render
from .models import Room


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Lets learn react!'},
#     {'id': 3, 'name': 'Frontend dev'}
# ]

# Funation base view


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}   #context dictionary
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context= {'room': room}
    return render(request, 'base/room.html', context)

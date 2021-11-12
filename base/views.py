from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Lets learn react!'},
    {'id': 3, 'name': 'Frontend dev'}
]

# Funation base view


def home(request):
    context = {'rooms': rooms} #context dictionary
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context= {'room': room}
    return render(request, 'base/room.html', context)

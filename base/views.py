from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id': 1, 'name': "Sweat in Chagauans"},
#     {'id': 2, 'name': "5-A-Side in Town!"},
#     {'id': 3, 'name': "Basketball Sweat in Lopinot"},
# ]

upids = [
    {'id': 1, 'name': "admin"},
    {'id': 2, 'name': "moderator"},
    {'id': 3, 'name': "user"},
]

sdets = [
    {'sid': 1, 'sn': 'NA'},
    {'sid': 2, 'sn': 'SA'},
    {'sid': 3, 'sn': 'EU'},
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms,
               'upids': upids,
               'sdets': sdets, }
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
            
    context = {'room': room,
               'sdets': sdets,
               }
    return render(request, 'base/room.html', context)


def upid(request, pk):
    upid = None
    for i in upids:
        if i['id'] == int(pk):
            upid = i
        context = {'upid': upid}
    return render(request, 'base/upid.html', context)


def sdet(request, pk):
    sdet = None
    for i in sdets:
        if i['sid'] == int(pk):
            sdet = i
        context = {'sdet': sdet}
    return render(request, 'base/sdet.html', context)

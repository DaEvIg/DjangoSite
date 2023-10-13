<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Главная страница приложения')


def cards(request):
    return HttpResponse(f'Карточки')


def cards_by_uuid(request, card_uuid):
    return HttpResponse(f'<h1>Карточка с uuid</h1><p>uuid: {card_uuid}</p>')


def cards_by_slug(request, card_slug):
    return HttpResponse(f'<h1>Карточка с slug</h1><p>slug: {card_slug}</p>')
>>>>>>> 00aea38 (add new file brics/urls.py)

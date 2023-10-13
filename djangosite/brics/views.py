from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Note

def index(request):
    return render(request, f'brics/post_list.html')


def cards(request):
    return HttpResponse(f'Карточки')


def cards_by_uuid(request, card_uuid):
    return HttpResponse(f'<h1>Карточка с uuid</h1><p>uuid: {card_uuid}</p>')


# def cards_by_slug(request, slug):
#     note_list = Note.objects.get(slug=slug)
#     return JsonResponse(request, f'<h1>Карточка с slug</h1><p>slug: {note_list}</p>')


def cards_by_slug(request, slug):
    note = get_object_or_404(Note, slug=slug)

    context = {
        'slug': note.slug,
        'name': note.name,
        'title': note.title,
        'text': note.text,
    }

    return HttpResponse(f'<h1>Карточка с slug</h1><p>slug: {context}</p>')
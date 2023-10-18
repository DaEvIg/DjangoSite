from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Note


def cards_by_slug(request, card_slug):
    note = Note.objects.get(slug=card_slug)
    return render(request, 'brics/post_list.html', context={'note': note})


def recovery(request):
    pass

def delited_list(request):
    pass

# получение данных из бд
def index(request):
    notes = Note.objects.all()
    users_list = User.objects.all()
    return render(request, "brics/index.html", {"notes": notes, 'users': users_list})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        note = Note()
       # User.user = request.POST.get("User")
        #note.name = request.POST.get("User")
        note.title = request.POST.get("title")
        note.text = request.POST.get("text")
        note.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        note = Note.objects.get(id=id)

        if request.method == "POST":
            note.title = request.POST.get("title")
            note.text = request.POST.get("text")
            note.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "brics/edit.html", {"note": note})
    except Note.DoesNotExist:
        return HttpResponseNotFound("<h2>Note not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
        return HttpResponseRedirect("/")
    except Note.DoesNotExist:
        return HttpResponseNotFound("<h2>Note not found</h2>")



from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Note


def cards_by_slug(request, card_slug):
    note = Note.objects.get(slug=card_slug)
    return render(request, 'brics/note.html', context={'note': note})


def deleted_list(request):
    del_list = Note.objects.deleted_only()
    return render(request, "brics/delete_list.html", {"del": del_list})

# получение данных из бд
def index(request):
    notes = Note.objects.all()
    users_list = User.objects.all()
    return render(request, "brics/index.html", {"notes": notes, 'users': users_list})

def show_notes_list(request):
    notes = Note.objects.all()
    users_list = User.objects.all()
    return render(request, "brics/post_list.html", {"notes": notes, 'users': users_list})

def soft_delete(request, id):
    note = Note.objects.get(pk=id)
    note.delete()
    return HttpResponseRedirect("/")

def undelete(request, id):
    del_notes_all = Note.deleted_objects.get(pk=id)
    del_notes_all.undelete()
    return HttpResponseRedirect("/")

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        note = Note()
        note.slug = request.POST.get("slug")
        note.name = request.POST.get('user1')
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


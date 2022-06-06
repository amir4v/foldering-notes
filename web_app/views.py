from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from FolderNote.models import Folder, Note


def index(request):
    folders = request.user.folder_set.all()
    return render(request, "web_app/index.html", {"folders":folders})


def create_folder(request):
    parent = request.POST.get("parent", None)
    name = request.POST.get("name")

    user = request.user # owner

    if parent:
        parent = Folder.objects.get(id=parent)
        user.folder_set.create(name=name, parent=parent)

        return redirect(f"/{parent.id}/notes")
    else:
        user.folder_set.create(name=name)
        return redirect("/")


def create_note(request, folder):
    if request.method == "GET":
        return render(request, "web_app/new_note.html", {"folder":folder})
    
    Folder.objects.get(id=folder).note_set.create(content=request.POST.get("content"))
    return redirect(f"/{folder}/notes")


def notes(request, folder): # shows: folders & notes
    folders = Folder.objects.filter(parent__id=folder)
    notes = Folder.objects.get(id=folder).note_set.all()
    return render(request, "web_app/folders_notes.html", {"folders":folders, "notes":notes, "folder":folder})
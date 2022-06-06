from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("create-folder", views.create_folder),
    path("create-note/<int:folder>", views.create_note),
    path("<int:folder>/notes", views.notes), # shows: folders & notes
]
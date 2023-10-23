from django.contrib import admin
from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.index),
    path('cards/<slug:card_slug>/', views.cards_by_slug),
    path('create/', views.create),
    path('deleted_list/', views.deleted_list),
    path('deleted_list/undelete/<int:id>/', views.undelete),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.soft_delete),
    path('post_list/', views.show_notes_list),
]

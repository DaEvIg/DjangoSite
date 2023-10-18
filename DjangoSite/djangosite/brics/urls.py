from django.contrib import admin
from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.index),
    path('cards/<slug:card_slug>/', views.cards_by_slug),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]

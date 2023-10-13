from django.contrib import admin
from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.index),
    path('cards/', views.cards),
    path('cards/<uuid:card_uuid>/', views.cards_by_uuid),
    path('cards/<slug:slug>/', views.cards_by_slug),
]

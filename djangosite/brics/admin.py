from django.contrib import admin
from .models import Note

@admin.register(Note)
class AuthorAdmin(admin.ModelAdmin):
    pass


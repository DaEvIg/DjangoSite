# from django.contrib import admin
# from .models import Note
#
#
# @admin.register(Note)
# class AuthorAdmin(admin.ModelAdmin):
#     pass



from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, SafeDeleteAdminFilter, highlight_deleted
from .models import Note


class NoteAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "highlight_deleted_field", "name", "title", "text") + SafeDeleteAdmin.list_display
    list_filter = ("title", SafeDeleteAdminFilter,) + SafeDeleteAdmin.list_filter
    field_to_highlight = "id"

admin.site.register(Note, NoteAdmin)
NoteAdmin.highlight_deleted_field.short_description = NoteAdmin.field_to_highlight
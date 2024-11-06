from django.contrib import admin

from api.models import PasteBin


# Register your models here.
@admin.register(PasteBin)
class PasteAdmin(admin.ModelAdmin):
    fields = ['id', 'content', 'is_locked', 'time_create', 'time_update', ]
    list_display = ('id', 'content', 'is_locked', 'time_create', 'time_update', )
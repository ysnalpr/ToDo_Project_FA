from django.contrib import admin
from .models import ToDo

# Register your models here.

@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'important', 'created', 'datecomplete', 'user']
    list_filter = ['created', 'datecomplete', 'user']
    search_fields = ['title', 'memo', 'user']
    list_editable = ('important',)
    raw_id_fields = ('user',)
    date_hierarchy = 'created'
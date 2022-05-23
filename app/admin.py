from django.contrib import admin

# Register your models here.
from app.models import Note

@admin.register(Note)
class noteA(admin.ModelAdmin):
    list_display = ['id','title','text','date']
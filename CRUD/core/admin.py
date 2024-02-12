from django.contrib import admin
from .models import MarvelModel

# Register your models here.
@admin.register(MarvelModel)
class MarvelAdmin(admin.ModelAdmin):
    list_display = ['id','name','heroic_name']
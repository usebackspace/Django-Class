from django.contrib import admin
from . models import Queryset
# Register your models here.
@admin.register(Queryset)
class QuerysetAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']
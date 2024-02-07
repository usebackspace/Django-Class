from django.contrib import admin
from . models import DcModel
# Register your models here.


@admin.register(DcModel)
class DcAdmin(admin.ModelAdmin):
    list_display =['id','name','heroic_name']
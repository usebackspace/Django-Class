from django.contrib import admin
from marvel.models import Marvel

@admin.register(Marvel)
class MarvelAdmin(admin.ModelAdmin):
    list_display =['id','name','heroic_name','city']

# admin.site.register(Marvel)
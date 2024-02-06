from django.urls import path
from savedata import views


urlpatterns = [
    path('marvel/',views.marvel)
]

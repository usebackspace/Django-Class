from django.urls import path
from . import views

urlpatterns = [
    path('pass/',views.password)
]

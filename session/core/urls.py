from django.urls import path
from . import views

urlpatterns = [
    path('getsession/',views.getsession),
    path('setsession/',views.setsession),
    path('deletesession/',views.deletesession),
]

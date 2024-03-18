from django.urls import path
from . import views

urlpatterns = [
    path('getcookies/',views.getcookies),
    path('setcookies/',views.setcookies),
    path('deletecookies/',views.deletecookies),
]

# We are in urls.py file of core app

from django.urls import path
from . import views

urlpatterns = [
    path('',views.base),
    path('about/',views.about),
    path('aboutt/<id>/',views.about,name='about')

]

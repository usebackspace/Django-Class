# We are in urls.py file of core app

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),


]

"""
URL configuration for Hero2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from marvel import views as m    # In both app we have same module name views.py, so we have to use alias of views
                                 # To recognize python that which views is from which app.
from dc import views as d
urlpatterns = [
    path('admin/', admin.site.urls),
    path('spiderman/',m.spiderman),
    path('ironman/',m.ironman),
    path('superman/',d.superman),
    path('batman/',d.batman),


]

from django.urls import path
from . import views

urlpatterns = [
    path('settestcookie/',views.settestcookie),
    path('testcookieworked/',views.testcookieworked),
    path('deletetestcookie/',views.deletetestcookie),
]

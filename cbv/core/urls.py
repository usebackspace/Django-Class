from django.urls import path
from . import views


urlpatterns = [
    path('fbv',views.fbv,name='fbv'),
    path('home',views.home,name='home'),
    path('form',views.form,name='form'),
    # path('temp',views.temp,name='temp'),
    path('temp',views.temp,{'template_name':'core/temp.html'},name='temp'),
    path('temp1',views.temp,{'template_name':'core/home.html'},name='temp1'),
    path('cbv',views.Cbv.as_view(),name='cbv'),
    path('homecl',views.Home.as_view(name='Stark'),name='homecl'),
    path('formcl',views.Formcls.as_view(),name='formcl'),
    # path('tempcl',views.Tempcl.as_view(),name='tempcl'),
    path('tempcl',views.Tempcl.as_view(template_name='core/temp.html'),name='tempcl'),


]

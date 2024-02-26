# We are in urls.py file of core app

from django.urls import path
from . import views
#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------------------
urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name='home'),

    path('about',views.about,name='about'),

    path('contact',views.contact,name='contact'),

    #------- Dog View Functions ------------
    # path('dog_categories',views.dog_categories,name='dogcategories'),
    path('dog_categories',views.DogCategoriesView.as_view(),name='dogcategories'),

    #------- Cat View Functions ------------
    # path('cat_categories',views.cat_categories,name='catcategories'),
    path('cat_categories',views.CatCategoriesView.as_view(),name='catcategories'),

    #------- Bird View Functions ------------
    path('bird_categories',views.bird_categories,name='birdcategories'),

    
    # path('pet_details',views.pet_details,name='petdetails'),
    path('pet_details/<int:id>/',views.PetDetailView.as_view(),name='petdetails'),
]

#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

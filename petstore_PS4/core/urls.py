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

    path('about/',views.about,name='about'),

    path('contact/',views.contact,name='contact'),

    #------- Dog View Functions ------------
    # path('dog_categories',views.dog_categories,name='dogcategories'),
    path('dog_categories/',views.DogCategoriesView.as_view(),name='dogcategories'),

    #------- Cat View Functions ------------
    # path('cat_categories',views.cat_categories,name='catcategories'),
    path('cat_categories/',views.CatCategoriesView.as_view(),name='catcategories'),

    #------- Bird View Functions ------------
    path('bird_categories/',views.bird_categories,name='birdcategories'),

    
    # path('pet_details',views.pet_details,name='petdetails'),
    path('pet_details/<int:id>/',views.PetDetailView.as_view(),name='petdetails'),

    path('registration/',views.registration,name='registration'),

    path('login/',views.log_in,name='login'),

    path('profile/',views.profile,name='profile'),

    path('logout/',views.log_out, name="logout"),

    path('changepassword/',views.changepassword, name="changepassword"),

    path('add_to_cart/<int:id>/',views.add_to_cart, name="addtocart"),

    path('view_cart/',views.view_cart, name="viewcart"),

    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),

    path('delete_quantity/<int:id>/', views.delete_quantity, name='delete_quantity'),

    path('delete_cart/<int:id>',views.delete_cart, name="deletecart"),
    

]

#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

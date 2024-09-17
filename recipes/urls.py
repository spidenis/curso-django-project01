from django.urls import path
from recipes.views import my_first_response, my_first_contact
 
urlpatterns = [
    path('', my_first_response),
    path('contact/', my_first_contact),
]

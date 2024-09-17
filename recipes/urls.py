from django.urls import path
from recipes.views import my_first_response
 
urlpatterns = [
    path('', my_first_response),
]

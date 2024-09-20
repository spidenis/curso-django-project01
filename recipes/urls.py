from django.urls import path
from . import views
 
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('app/recipes/<int:id>/', views.recipes, name="recipe"),
]

from django.shortcuts import render


# Create your views here.
def my_first_response(request):
    return render(request, 'recipes/home.html')
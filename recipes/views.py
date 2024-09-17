from django.shortcuts import render


# Create your views here.
def my_first_response(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Valdenilson'
    })

def my_first_contact(request):
    return render(request, 'recipes/contact.html', context={
        'name': '68981159337'
    })
from django.shortcuts import render, get_object_or_404
from .models import Recipe


# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published = True
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(categegory__id=category_id, is_published=True).order_by('-id')
    
    if not recipes:
        return render(request, 'recipes/pages/page_not_found.html', context={
        'title': f'Category Not Found',
        }, status=404)
    else:
        return render(request, 'recipes/pages/category.html', context={
            'recipes': recipes,
            'title': f'{recipes.first().categegory.name}  - Category |'
        })

def recipes(request, id):

    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    #recipe = Recipe.objects.filter(id=id)[:1].get()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
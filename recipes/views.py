from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import Http404
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

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | 
            Q(description__icontains=search_term) |
            Q(preparation_steps__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': recipes,
    })
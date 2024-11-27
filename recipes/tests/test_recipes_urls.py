from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):
    
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')

        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})

        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_details_url_is_correct(self):
        details_url = reverse('recipes:recipe', kwargs={'id': 1})

        self.assertEqual(details_url, '/recipes/1/')
    
    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')
from django.test import TestCase
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setUp(self):
        return super().setUp()

    def make_recipe_category(self,name='Category'):
        return Category.objects.create(name=name) 
    
    def make_recipe_author(
            self,
            first_name='user',
            last_name='name',
            username='username',
            password='13921',
            email='username@gmail.com',
        ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
            self,
            categegory_data = None,
            author_data = None,
            title = 'Recipe Title' ,
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe preparation steps',
            preparation_steps_is_html = False,
            is_published = True,
    ):
        if categegory_data is None:
            categegory_data = {}
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            categegory = self.make_recipe_category(**categegory_data),
            author = self.make_recipe_author(**author_data),
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
        )
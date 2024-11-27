from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized



class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
            recipe = Recipe(
            categegory = self.make_recipe_category(name='Test Default Category'),
            author = self.make_recipe_author(username='newusertest'),
            title = 'Recipe Title Now' ,
            description = 'Recipe Description',
            slug = 'recipe-slug-for_no_defaults',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe preparation steps',
         )
            recipe.full_clean()
            recipe.save()
            return recipe
    
    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ]
    )
    def test_recipe_fields_max_length(self, field, max_length):
            setattr(self.recipe, field, 'A' * (max_length + 1))
            with self.assertRaises(ValidationError):
                self.recipe.full_clean()
    
    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()

        self.assertFalse(recipe.preparation_steps_is_html, msg='Recipe preparation_steps_is_html is not False')
    
    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()

        self.assertFalse(recipe.is_published, msg='Recipe is_published is not False')
    
    def test_recipe_string_representation(self):
         needed = 'Testing Representation'
         self.recipe.title = 'Testing Representation'
         self.recipe.full_clean()
         self.recipe.save()
         self.assertEqual(
              str(self.recipe), needed,
              msg=f'Recipe string representation must be "{needed}" but "{self.recipe}" was recived.'
            )
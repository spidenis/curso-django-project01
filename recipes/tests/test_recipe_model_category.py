from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError



class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self):
        self.categegory = self.make_recipe_category()
        return super().setUp()

    def test_recipe_category_model_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.categegory),
            self.categegory.name
        )

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        self.categegory.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.categegory.full_clean()
from django.db import models

# Create your models here.
class ingredients(models.Model):
    ingredient_name = models.CharField(max_length=50)
    calories = models.PositiveSmallIntegerField()
    total_fat = models.FloatField()
    saturated_fat = models.FloatField()
    polyunsaturated_fat = models.FloatField()
    monounsaturated_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    potassium = models.FloatField()
    total_carb = models.FloatField()
    dietary_fiber = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()

    class Meta:
        db_table = "ingredients"

class recipes(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_ingredients = models.JSONField()
    recipe_type = models.CharField(max_length=20)

    class Meta:
        db_table = "recipes"
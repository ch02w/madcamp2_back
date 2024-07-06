from django.db import models


class Ingredients(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=255)
    food_category = models.CharField(max_length=7)
    unit = models.CharField(max_length=2)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=255)
    recipe_content = models.TextField()

    class Meta:
        managed = False
        db_table = 'recipe'


class RecipeDetail(models.Model):
    recipe_id = models.IntegerField(primary_key=True)  # The composite primary key (recipe_id, food_id) found, that is not supported. The first column is selected.
    food_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recipe_detail'
        unique_together = (('recipe_id', 'food_id'),)

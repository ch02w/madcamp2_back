# recipes/serializers.py
from rest_framework import serializers
from .models import Recipe, RecipeDetail, Ingredients

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class RecipeDetailSerializer(serializers.ModelSerializer):
    food_name = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()

    class Meta:
        model = RecipeDetail
        fields = '__all__'

    def get_food_name(self, obj):
        ingredient = Ingredients.objects.get(food_id=obj.food_id)
        return ingredient.food_name

    def get_unit(self, obj):
        ingredient = Ingredients.objects.get(food_id=obj.food_id)
        return ingredient.unit


class RecipeSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_details(self, obj):
        details = RecipeDetail.objects.filter(recipe_id=obj.recipe_id)
        return RecipeDetailSerializer(details, many=True).data

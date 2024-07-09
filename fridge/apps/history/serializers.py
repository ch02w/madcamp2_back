from rest_framework import serializers
from .models import History, HistoryDetail
from apps.recipes.models import Recipe  # assuming you have a Recipe model
from apps.ingredients.models import Ingredients  # assuming you have an Ingredients model

class HistoryDetailSerializer(serializers.ModelSerializer):
    food_name = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()

    class Meta:
        model = HistoryDetail
        fields = ['detail_id', 'food_id', 'amount', 'food_name', 'unit']

    def get_food_name(self, obj):
        try:
            ingredient = Ingredients.objects.get(food_id=obj.food_id)
            return ingredient.food_name
        except Ingredients.DoesNotExist:
            return ''

    def get_unit(self, obj):
        try:
            ingredient = Ingredients.objects.get(food_id=obj.food_id)
            return ingredient.unit
        except Ingredients.DoesNotExist:
            return ''

class HistorySerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()
    recipe_name = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['history_id', 'user_id', 'recipe_id', 'time', 'recipe_name', 'ingredients']

    def get_ingredients(self, obj):
        details = HistoryDetail.objects.filter(history_id=obj.history_id)
        return HistoryDetailSerializer(details, many=True).data

    def get_recipe_name(self, obj):
        if obj.recipe_id:
            try:
                recipe = Recipe.objects.get(recipe_id=obj.recipe_id)
                return recipe.recipe_name
            except Recipe.DoesNotExist:
                return 'Unknown Recipe'
        return '커스텀 레시피'

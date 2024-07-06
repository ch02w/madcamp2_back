from rest_framework import serializers
from .models import Recipe, RecipeDetail, Ingredients

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeDetail
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_details(self, obj):
        details = RecipeDetail.objects.filter(recipe_id=obj.recipe_id)
        return RecipeDetailSerializer(details, many=True).data

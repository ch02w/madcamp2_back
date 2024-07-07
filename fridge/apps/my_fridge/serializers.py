# my_fridge/serializers.py
from rest_framework import serializers
from .models import MyFridge, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MyFridgeSerializer(serializers.ModelSerializer):
    food_name = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    food_category = serializers.SerializerMethodField()

    class Meta:
        model = MyFridge
        fields = '__all__'

    def get_food_name(self, obj):
        return Ingredient.objects.get(food_id=obj.food_id).food_name

    def get_unit(self, obj):
        return Ingredient.objects.get(food_id=obj.food_id).unit

    def get_food_category(self, obj):
        return Ingredient.objects.get(food_id=obj.food_id).food_category

class MyFridgeCreateSerializer(serializers.ModelSerializer):
    food_id = serializers.IntegerField()

    class Meta:
        model = MyFridge
        fields = ['food_id', 'amount', 'expiration_date']

    def create(self, validated_data):
        food_id = validated_data.pop('food_id')
        ingredient = Ingredient.objects.get(food_id=food_id)
        my_fridge = MyFridge.objects.create(food_id=food_id, **validated_data)
        return my_fridge

class MyFridgeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFridge
        fields = ['amount', 'expiration_date']

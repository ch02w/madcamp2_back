from rest_framework import serializers
from .models import MyFridge, Ingredients

class MyFridgeSerializer(serializers.ModelSerializer):
    food_name = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    food_category = serializers.SerializerMethodField()

    class Meta:
        model = MyFridge
        fields = '__all__'

    def get_food_name(self, obj):
        return Ingredients.objects.get(food_id=obj.food_id).food_name

    def get_unit(self, obj):
        return Ingredients.objects.get(food_id=obj.food_id).unit
    
    def get_food_category(self, obj):
        return Ingredients.objects.get(food_id=obj.food_id).food_category

class MyFridgeCreateSerializer(serializers.Serializer):
    food_id = serializers.IntegerField()
    amount = serializers.IntegerField()
    expiration_date = serializers.DateField()

class MyFridgeUpdateSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=False)
    expiration_date = serializers.DateField(required=False)

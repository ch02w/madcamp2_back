# my_fridge/serializers.py
from rest_framework import serializers
from .models import MyFridge

class MyFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFridge
        fields = '__all__'

class MyFridgeCreateSerializer(serializers.Serializer):
    food_id = serializers.IntegerField()
    amount = serializers.IntegerField()
    expiration_date = serializers.DateTimeField()

class MyFridgeUpdateSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=False)
    expiration_date = serializers.DateTimeField(required=False)
    history_id = serializers.IntegerField(required=False)

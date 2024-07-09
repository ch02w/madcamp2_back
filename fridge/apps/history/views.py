from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import History, HistoryDetail
from apps.recipes.models import Recipe  # assuming you have a Recipe model
from apps.ingredients.models import Ingredients  # assuming you have an Ingredients model
from .serializers import HistorySerializer, HistoryDetailSerializer
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
import json

class HistoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return History.objects.filter(user_id=user_id)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        data = request.data
        time = parse_datetime(data['time'])
        recipe_id = data['recipe_id']
        details = data['details'][2:-1].split(', ')
        print(details)
        history = History.objects.create(user_id=user_id, time=time, recipe_id=recipe_id)
        for detail in details:
            detail = json.loads(detail)
            food_id = detail['food_id']
            amount = detail['amount']
            HistoryDetail.objects.create(history_id=history.history_id, food_id=food_id, amount=amount)
        return Response({'status': 'success', 'history_id': history.history_id}, status=201)

class FoodHistoryAPIView(APIView):
    def get(self, request, user_id, food_id, *args, **kwargs):
        histories = History.objects.filter(user_id=user_id)
        history_ids = [h.history_id for h in histories]
        details = HistoryDetail.objects.filter(food_id=food_id, history_id__in=history_ids)
        result = []

        for detail in details:
            history = History.objects.get(history_id=detail.history_id)
            recipe_name = '커스텀'
            if history.recipe_id:
                try:
                    recipe = Recipe.objects.get(recipe_id=history.recipe_id)
                    recipe_name = recipe.recipe_name
                except Recipe.DoesNotExist:
                    pass
            result.append({
                'recipe_name': recipe_name,
                'time': history.time,
                'food_name': Ingredients.objects.get(food_id=food_id).food_name,
                'amount': detail.amount,
                'unit': Ingredients.objects.get(food_id=food_id).unit,
            })
        
        return Response(result, status=status.HTTP_200_OK)

class HistoryDetailCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        history_id = self.kwargs['history_id']
        data = request.data
        food_id = data['food_id']
        amount = data['amount']
        history_detail = HistoryDetail.objects.create(history_id=history_id, food_id=food_id, amount=amount)
        return Response({'status': 'success', 'history_detail_id': history_detail.detail_id}, status=201)

# my_fridge/urls.py
from django.urls import path
from .views import MyFridgeListCreateAPIView, MyFridgeUpdateDeleteAPIView

urlpatterns = [
    path('<str:userId>/', MyFridgeListCreateAPIView.as_view(), name='fridge-ingredients-list-create'),
    path('ingredients/<int:fridge_id>/', MyFridgeUpdateDeleteAPIView.as_view(), name='fridge-ingredients-update-delete'),
]

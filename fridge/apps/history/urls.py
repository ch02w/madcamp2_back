from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.HistoryListCreateAPIView.as_view(), name='history_list_create'),
    path('<int:user_id>/<int:food_id>/', views.FoodHistoryAPIView.as_view(), name='get_food_history'),
    path('detail/<int:history_id>/', views.HistoryDetailCreateAPIView.as_view(), name='history_detail_list'),
]

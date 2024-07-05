from django.urls import path
from .views import kakao_login

urlpatterns = [
    path('login/', kakao_login),
]

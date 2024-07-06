from django.urls import path
from .views import kakao

urlpatterns = [
    path('kakao/', kakao, name='kakao'),
]

from django.urls import path
from .views import save_user

urlpatterns = [
    path('save_user/', save_user, name='save_user'),
]

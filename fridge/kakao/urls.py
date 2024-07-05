from django.urls import path
from .views import SaveUserInfoView

urlpatterns = [
    path('save_user/', SaveUserInfoView.as_view(), name='save_user'),
]

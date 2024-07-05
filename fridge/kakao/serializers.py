from rest_framework import serializers
from .models import KakaoUser

class KakaoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KakaoUser
        fields = ['kakao_id', 'nickname']

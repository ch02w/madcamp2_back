from django.db import models

class KakaoUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
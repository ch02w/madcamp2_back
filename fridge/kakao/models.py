from django.db import models

class User(models.Model):
    kakao_id = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
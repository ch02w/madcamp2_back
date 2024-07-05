from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname
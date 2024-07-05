from django.db import models


class Users(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    nickname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'

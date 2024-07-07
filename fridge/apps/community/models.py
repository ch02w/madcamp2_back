from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    nickname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    writer_id = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'board'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    board_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    writer_id = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'comments'

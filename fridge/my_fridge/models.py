# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    nickname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class MyFridge(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)  # The composite primary key (user_id, food_id) found, that is not supported. The first column is selected.
    food_id = models.IntegerField()
    amount = models.IntegerField()
    expiration_date = models.DateTimeField()
    history_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'my_fridge'
        unique_together = (('user_id', 'food_id'),)


class Ingredients(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=255)
    food_category = models.CharField(max_length=7)
    unit = models.CharField(max_length=2)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'

from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    nickname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class Ingredient(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=255)
    food_category = models.CharField(max_length=7)
    unit = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'ingredients'


class MyFridge(models.Model):
    user_id = models.CharField(max_length=255)
    food_id = models.IntegerField()
    amount = models.IntegerField()
    expiration_date = models.DateField(blank=True, null=True)
    fridge_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'my_fridge'

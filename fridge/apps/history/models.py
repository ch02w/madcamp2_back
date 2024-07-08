from django.db import models


class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255)
    recipe_id = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'history'


class HistoryDetail(models.Model):
    detail_id = models.IntegerField(primary_key=True)
    history_id = models.IntegerField()
    food_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_detail'


# ingredients/models.py

from django.db import models

class Ingredients(models.Model):
    FOOD_CATEGORIES = [
        ('과일', '과일'),
        ('채소', '채소'),
        ('쌀/잡곡/견과', '쌀/잡곡/견과'),
        ('정육', '정육'),
        ('계란', '계란'),
        ('수산물', '수산물'),
        ('유제품', '유제품'),
        ('밀키트', '밀키트'),
        ('반찬', '반찬'),
        ('양념/오일', '양념/오일'),
        ('생수', '생수'),
        ('기타', '기타'),
    ]
    
    UNITS = [
        ('개', '개'),
        ('ml', 'ml'),
        ('g', 'g'),
    ]

    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=255)
    food_category = models.CharField(max_length=20, choices=FOOD_CATEGORIES)
    unit = models.CharField(max_length=10, choices=UNITS)
    image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.food_name
    
    class Meta:
        managed = False
        db_table = 'ingredients'

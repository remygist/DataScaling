from django.db import models
import datetime

class Discoverer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Plant(models.Model):
    name = models.CharField(max_length=100)
    bloom_start = models.DateField(default=datetime.date(2000, 1, 1))
    bloom_end = models.DateField(default=datetime.date(2000, 12, 31)) 
    planting_season_start = models.DateField(default=datetime.date(2000, 4, 1))
    planting_season_end = models.DateField(default=datetime.date(2000, 9, 30)) 
    discoverer = models.ForeignKey(Discoverer, on_delete=models.SET_NULL, null=True)
    
from django.db import models

class Discoverer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Plant(models.Model):
    name = models.CharField(max_length=100)
    bloom_start = models.DateField
    bloom_end = models.DateField
    planting_season_start = models.DateField
    planting_season_end = models.DateField
    discoverer = models.ForeignKey(Discoverer, on_delete=models.SET_NULL, null=True)
    
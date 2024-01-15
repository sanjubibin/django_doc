from django.db import models

# Create your models here.

class LocationUSADataModel(models.Model):
    # id = models.AutoField(primary_key=True)
    city_or_country = models.CharField(default = None, max_length = 50)
    type = models.CharField(default = None, max_length = 50)
    state = models.CharField(default = None, max_length = 50)
    state_name = models.CharField(default = None, max_length = 50)
    county = models.CharField(default = None, max_length = 50)
    lattitude = models.CharField(default = None, max_length = 50)
    longitude = models.CharField(default = None, max_length = 50)
    population = models.CharField(default = None, max_length = 50)



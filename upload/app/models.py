from django.db import models

class Datamodels(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
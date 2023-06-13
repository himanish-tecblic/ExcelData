from django.db import models

class RandomData(models.Model):
    name = models.CharField(max_length=200)
class Datamodels(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    random = models.ForeignKey(RandomData, verbose_name=(""), on_delete=models.CASCADE,null=True)
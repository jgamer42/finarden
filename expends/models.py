from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expend(models.Model):
    detail = models.TextField()
    amount = models.FloatField()
    date = models.DateTimeField()
    where = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Income(models.Model):
    detail = models.TextField()
    amount = models.FloatField()
    date = models.DateTimeField()
    source = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Bill(models.Model):
    detail = models.TextField()
    duration = models.IntegerField()
    where = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cutoff = models.IntegerField()
    amount = models.FloatField()
    active = models.BooleanField()
from django.db import models

# Create your models here.

class Tip(models.Model):
    detail = models.TextField()
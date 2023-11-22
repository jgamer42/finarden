from django.db import models

# Create your models here.

class Tip(models.Model):
    detail = models.TextField()
    active = models.BooleanField(null=True)
    created = models.DateTimeField(null=True,auto_now_add=True)
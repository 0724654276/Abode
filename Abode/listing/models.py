from django.db import models

# Create your models here.

class land(models.Model):
    location = models.CharField(max_length= "64", blank = False)
    Size = models.IntegerField()
    
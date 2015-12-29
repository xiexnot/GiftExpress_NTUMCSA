from django.db import models

# Create your models here.
class Female(models.Model):
    identify = models.IntegerField()
    name = models.CharField(default = "noname",max_length=50)
    exchange_flag = models.BooleanField(default=False)
    sex = models.CharField(default="Female", max_length=10)

class Male(models.Model):
    identify = models.IntegerField()
    name = models.CharField(default = "noname",max_length=50)
    exchange_flag = models.BooleanField(default=False)
    sex = models.CharField(default="Male",max_length=10)

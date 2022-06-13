from importlib.resources import path
from operator import methodcaller
from django.db import models
from django.db.models import Count




class insertable(models.Model):
    method= models.CharField(max_length=200)
    path= models.CharField(max_length=200)
    date= models.CharField(max_length=200)
    day= models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    company_id = models.CharField(max_length=200)
    client_id = models.IntegerField(default=0)
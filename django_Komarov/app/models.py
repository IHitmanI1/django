from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    foto =  models.CharField(max_length=10)

# Create your models here.

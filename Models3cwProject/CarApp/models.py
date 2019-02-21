from django.db import models
from datetime import datetime

# Create your models here.
class Car(models.Model):
    make=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    year=models.DateField(default=datetime.now())

    def __str__(self):
        return self.make
    # def __str__(self):
    #     return self.model
    # def __str__(self):
    #     return self.year

class Book(models.Model):
    name=models.CharField(max_length=100)
    pagenum=models.CharField(max_length=100)
    pubdate=models.DateField(default=datetime.now())
    genre=models.CharField(max_length=15)

    def __str__(self):
        return self.name

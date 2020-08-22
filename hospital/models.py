from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
# Create your models here.



class Branch(models.Model):
    name = models.CharField(max_length=50)
    rate = models.IntegerField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mail = models.EmailField(default="")
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=150)
    registered = models.DateField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mail = models.EmailField(default="")
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

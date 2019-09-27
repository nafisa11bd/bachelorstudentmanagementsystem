from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sturoll(models.Model):
    name=models.CharField(max_length=20)


class CSE3101(models.Model):
    roll=models.IntegerField(max_length=10)
    mark=models.IntegerField(max_length=10)

class CSE3105(models.Model):
    roll = models.IntegerField(max_length=10)
    mark = models.IntegerField(max_length=10)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

class CSE3107(models.Model):
    roll = models.IntegerField(max_length=10)
    mark = models.IntegerField(max_length=10)
    file = models.FileField(upload_to='abc/')

class CSE3109(models.Model):
    roll = models.IntegerField(max_length=10)
    mark = models.IntegerField(max_length=10)
    file = models.FileField(upload_to='abc/')




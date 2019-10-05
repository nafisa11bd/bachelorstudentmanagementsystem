from django.db import models



# Create your models here.
class Sturoll(models.Model):
    name=models.CharField(max_length=20)


class CSE3101(models.Model):
    roll=models.IntegerField(primary_key=True)
    ct1mark=models.IntegerField(max_length=10,blank=True)
    ct2mark = models.IntegerField(max_length=10, blank=True)
    ct3mark = models.IntegerField(max_length=10, blank=True)
    ct4mark = models.IntegerField(max_length=10, blank=True)

class CSE3105(models.Model):
    roll = models.IntegerField(max_length=10)
    mark = models.IntegerField(max_length=10)


class CSE3107(models.Model):
    roll = models.IntegerField(max_length=10)
    mark = models.IntegerField(max_length=10)
    file = models.FileField(upload_to='abc/')

class CSE3109(models.Model):
    roll = models.IntegerField(max_length=10)
    mark = models.IntegerField(max_length=10)
    file = models.FileField(upload_to='abc/')




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
    def bestavg(self):
        a = self.ct1mark+self.ct2mark+self.ct3mark+self.ct4mark
        b = min(self.ct1mark,self.ct2mark,self.ct3mark,self.ct4mark)
        c = a - b
        d = int(c/3)
        if d<c/3:
            d=d+1
        return d

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




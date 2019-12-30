from django.db import models


class Courseregister(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dept = models.CharField(max_length=50)
    email=models.EmailField(max_length=256,null=True)
    year = models.IntegerField(default=0)
    semester = models.IntegerField(default=0)
    roll = models.IntegerField(default=0)
    regno = models.IntegerField(default=0)
    pec =models.DecimalField(max_digits = 5, decimal_places = 2)
    cno1 = models.CharField(max_length=10)
    cname1 = models.CharField(max_length=100)
    cno2 = models.CharField(max_length=10)
    cname2 = models.CharField(max_length=100)
    cno3 = models.CharField(max_length=10)
    cname3 = models.CharField(max_length=100)
    cno4 = models.CharField(max_length=10)
    cname4 = models.CharField(max_length=100)
    cno5 = models.CharField(max_length=10)
    cname5 = models.CharField(max_length=100)

    def __str__(self):  
        return f'{self.fname} Profile'
    
    def save(self, *args, **kwargs):
        super().save()



class Courseregister2(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dept = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    semester = models.IntegerField(default=0)
    roll = models.IntegerField(default=0)
    regno = models.IntegerField(default=0)
    pec =models.DecimalField(max_digits = 5, decimal_places = 2)
    cno1 = models.CharField(max_length=10)
    cname1 = models.CharField(max_length=100)
    cno2 = models.CharField(max_length=10)
    cname2 = models.CharField(max_length=100)
    cno3 = models.CharField(max_length=10)
    cname3 = models.CharField(max_length=100)
    cno4 = models.CharField(max_length=10)
    cname4 = models.CharField(max_length=100)
    cno5 = models.CharField(max_length=10)
    cname5 = models.CharField(max_length=100)

    def __str__(self):   #need to know how it work
        return f'{self.fname} Profile'
    
    def save(self, *args, **kwargs):
        super().save()

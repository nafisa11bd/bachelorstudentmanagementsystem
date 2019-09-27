from django.db import models
from django.contrib.auth.models import User

class result(models.Model):
    title=models.CharField(max_length=255)
    file=models.FileField(upload_to='files/')
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title





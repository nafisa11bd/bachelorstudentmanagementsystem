from django.db import models

# Create your models here.
class days(models.Model):
    roll=models.IntegerField(primary_key=True)
    classes=models.IntegerField(blank=True)
    def get_percentage(self):
        return self.classes*100/39

  

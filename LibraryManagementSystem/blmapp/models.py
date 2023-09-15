from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=50)
    leaseCost = models.IntegerField()
    
    def __str__(self):
        return self.title
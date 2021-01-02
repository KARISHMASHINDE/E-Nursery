from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    
    
class Plant(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class NurseryPlant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nurseryName = models.CharField(max_length=100)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='PlantImage')
    price = models.FloatField()
    
    
    def __str__(self):
        return self.nurseryName


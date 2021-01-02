from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    
    
class Plant(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class NurseryDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nurseryName = models.CharField(max_length=100)

    
    def __str__(self):
        return self.nurseryName
    
class NurseryPlant(models.Model):
    nurseryName = models.ForeignKey(NurseryDetails,on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='PlantImage')
    price = models.FloatField()
    
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    items = models.ManyToManyField(NurseryPlant)
    quantity = models.IntegerField()
    

    



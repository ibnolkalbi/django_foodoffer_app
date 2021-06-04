from django.db import models

# Create your models here.
class Post(models.Model):
    password = models.CharField(max_length=20)
    reasturantName = models.CharField(max_length=30)
    dishName = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    
    image = models.ImageField(null=True, blank = True)
    
    def __str__(self):
        return self.reasturantName

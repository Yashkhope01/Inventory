from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=55)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    
    def __str__(self):
        return self.name
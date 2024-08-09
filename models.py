from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class product(models.Model):
    productname = models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images')

class Carts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    quantity = models.IntegerField()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()





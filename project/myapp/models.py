from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category_image")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty  =models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="product_image")


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    
    def subTotal(self):
        return self.product.price*self.qty
    
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    
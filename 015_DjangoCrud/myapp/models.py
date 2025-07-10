from django.db import models


class Dept(models.Model):
    name = models.CharField(max_length=20)

# Create your models here.
class Student(models.Model):
    dept= models.ForeignKey(Dept,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    img = models.ImageField(upload_to="profiles", null=True)






# class Category(models.Model):
#     name = models.CharField(max_length=20)


# class Product(models.Model):
#     name = models.CharField(max_length=20)
#     price = models.FloatField()
#     qty = models.IntegerField()
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)



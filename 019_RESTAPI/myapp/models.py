from django.db import models

# Create your models here.
class Stduent(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()


class Emp(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    salary = models.FloatField()
    dept =models.CharField(max_length=50)



class Author(models.Model):
    name = models.CharField(max_length=20)
    education = models.CharField(max_length=50)


class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()

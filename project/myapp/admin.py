from django.contrib import admin
from myapp.models import *
# Register your models here.

class CategoryModel(admin.ModelAdmin):
    list_display=("id","name","image")

class ProductModel(admin.ModelAdmin):
    list_display=("id","category","name","price","qty","description","image")

admin.site.register(Category,CategoryModel)
admin.site.register(Product,ProductModel)
admin.site.register(Cart)

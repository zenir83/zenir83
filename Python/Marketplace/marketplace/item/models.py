from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta: # Django class for order and other model related functions
        ordering =('name', )
        verbose_name_plural = "Categories" # make the categories menu item spelling correct

    def __str__(self):
        return self.name # show the category instead of 'category object'

class Item(models.Model):
    category = models.ForeignKey(Category, related_name = 'items', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'item_images', blank = True, null = True )
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User, related_name='items', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
       
    def __str__(self):
        return self.name # show the category instead of 'category object'
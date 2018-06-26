# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 250)
    
    def __str__(self): 
        return self.location

class Category(models.Model):
    category = models.CharField(max_length = 250) 

    def __str__(self):
        return self.category

class Image(models.Model):
    image = models.ImageField(upload_to='images-posted/')
    image_name= models.CharField(max_length = 250)
    image_location=models.ForeignKey(Location)
    image_category=models.ForeignKey(Category)

    def __str__(self):
        return self.image_name


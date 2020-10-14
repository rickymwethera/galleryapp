from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = '', null = True, blank = True)
    name = models.CharField(max_length=20)	   
    description = models.CharField(max_length=100)	    
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null='True', blank=True)	    
    location = models.ForeignKey('Location', on_delete = models.CASCADE, null='True', blank=True)

from django.db import models

# Create your models here.

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description
    
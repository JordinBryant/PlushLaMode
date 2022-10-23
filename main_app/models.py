from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
SIZES = (
    ('S','Small'),
    ('M', 'Medium'),
    ('L','Large'),
)



class Dress(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    color = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000)
    # accessories = models.ManyToManyField(Accessory)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name   

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dress_id': self.id})

class Accessory(models.Model):
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    img_url = models.CharField(max_length=1000)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})        
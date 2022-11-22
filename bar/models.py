from django.db import models

# Create your models here.
class Triangle(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Oval(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Round(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Diamond(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Oblong(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Square(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Heart(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')


 

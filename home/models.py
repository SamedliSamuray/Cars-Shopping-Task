from django.db import models
# Create your models here.

class Owner(models.Model):
    name=models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    gallery=models.TextField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.gallery
    
class Car(models.Model):
    owner=models.OneToOneField(Owner,on_delete=models.CASCADE,related_name='owner')
    brand=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    gallery=models.ForeignKey(Gallery,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return f'{self.brand} - - {self.model}'
    
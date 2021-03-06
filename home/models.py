from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 250)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    content = models.TextField()
    contact_date = models.DateField(auto_now_add=True, blank=True)
    contact_time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self): 
        return '' + self.name + ''



class Enquire(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    contact_date = models.DateField(auto_now_add=True, blank=True)
    contact_time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self): 
        return '' + self.name + ''
    
    

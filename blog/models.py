from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=20)
    content = RichTextField(blank = True, null = True)
    slug = models.CharField(max_length=20)
    Created_date = models.DateField(blank=True)
    

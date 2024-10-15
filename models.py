from django.db import models
class Jpeople(models.Model):
    yourtext = models.TextField(max_length=5000)
    fileup = models.FileField(upload_to= 'Jpeople/',max_length=250,null=True,default=None)

# Create your models here.

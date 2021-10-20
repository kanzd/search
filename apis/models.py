from django.db import models

# Create your models here.



class Search(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=3000)
    items=models.CharField(max_length=3000)
    address=models.CharField(max_length=3000)
    pincode=models.CharField(max_length=3000)
    
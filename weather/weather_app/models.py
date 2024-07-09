from django.db import models

class New_user(models.Model):
    username=models.CharField(max_length=200,blank=False)
    email=models.EmailField(blank=False)

# Create your models here.

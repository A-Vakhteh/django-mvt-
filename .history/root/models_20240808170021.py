from django.db import models
from django.contrib.auth.models import User



class services(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    class META:
        ordering =('created_at',)

class trainer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    models.ImageField(upload_to="trainer", default="default.jpg")
    skills = models.ManyToManyField


class skills(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class META:
        ordering =('created_at',)
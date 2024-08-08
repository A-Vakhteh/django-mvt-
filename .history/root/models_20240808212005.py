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
        
class skills(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class META:
        ordering =('created_at',)        

class trainer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="trainer", default="default.jpg")
    skills = models.ManyToManyField(skills)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.user.username
        
    class META:
        ordering = ('created_at',)

class property(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    class META:
        ordering =('created_at',)    
class fee(models.Model):
    name = models.CharField(max_length =100)
    content = models.TextField()
    fee = models.FloatField(default=0)
    property = models.ManyToManyField(property)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('creat_at',)

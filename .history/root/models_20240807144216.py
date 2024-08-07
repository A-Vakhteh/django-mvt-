from django.db import models



class services(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)


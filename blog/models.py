from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=140, blank = True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    capa = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title
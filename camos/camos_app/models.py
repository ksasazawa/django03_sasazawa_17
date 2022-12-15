from django.db import models
from django.contrib.auth import get_user, get_user_model

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    job = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    body = models.TextField()
    agent = models.CharField(max_length=255)
    data_added = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    
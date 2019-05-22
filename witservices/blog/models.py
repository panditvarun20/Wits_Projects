from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.CharField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=true, null=true)

from django.db import models
from django.utils import timezone

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='',null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    goodmember = models.CharField(max_length=100, null=True, blank=True, default='a')
    created_at = models.DateTimeField('作成日', default=timezone.now)

class ProfileModel(models.Model):
    url_code =models.CharField(max_length=100,null=True, blank=True)
    author =models.CharField(max_length=100,null=True, blank=True)
    icon = models.ImageField(upload_to='')
    introduce = models.TextField(null=True, blank=True)

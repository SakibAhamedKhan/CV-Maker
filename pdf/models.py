from django.db import models
from django.conf import settings
# Create your models here.

class CV(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previouse_work = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    language = models.TextField(max_length=200, default='')
    image = models.ImageField(upload_to='cv', default='profilepic.jpg')
    project = models.TextField(max_length=1000, default='')
    def __str__(self) -> str:
        return self.name
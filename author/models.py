from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=5)
    birth_date = models.DateField(null=True, blank=True)
    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    country = models.CharField(max_length=100, default='')
    education = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=200 , default='')

    def __str__(self) -> str:
        return self.user.username
    

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    time = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} {self.email} {self.time}'
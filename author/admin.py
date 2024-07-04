from django.contrib import admin
from .models import CustomUser, UserInfo
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserInfo)
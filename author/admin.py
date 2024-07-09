from django.contrib import admin
from .models import CustomUser, UserInfo, ContactUs
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserInfo)
admin.site.register(ContactUs)

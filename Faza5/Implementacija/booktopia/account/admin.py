from django.contrib import admin

from .models import UserBase

# we register our costum user
admin.site.register(UserBase)

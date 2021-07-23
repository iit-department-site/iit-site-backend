from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNet

admin.site.register(UserNet, UserAdmin)
# Register your models here.

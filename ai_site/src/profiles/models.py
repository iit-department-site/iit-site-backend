from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from src.core.enums.profiles import Gender


class UserNet(AbstractUser):
    """Custom user model"""

    middle_name = models.CharField(max_length=50, blank=True)
    first_login = models.DateTimeField(auto_now_add=True, null=True)
    phone = models.CharField(
        max_length=40,
    )
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(
        max_length=500, null=True, blank=True,
        validators=(
            RegexValidator(regex='^(http(s?):\/\/)?(www\.)?github\.([a-z])+\/([A-Za-z0-9]{1,})+\/?$'),
        ))
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=Gender.choices(), default="MALE", max_length=7)
    technology = models.ManyToManyField('Technology', related_name='user', blank=True)


class Technology(models.Model):
    """Technology model"""
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='technology/', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class RegisterUsers(models.Model):
    name = models.CharField(
        max_length=30, blank=False, null=False
    )
    email = models.CharField(
        max_length= 30, blank=False, null= False
    )
    password = models.CharField(
        max_length=16, blank=False, null=False
    )
    userId = models.CharField(
        max_length=16, blank=False,null=False
    )
    createdAt = models.DateTimeField(
        null=False, blank=False
    )
    updatedAt = models.DateTimeField(
        null=False, blank=False
    )
    status = models.TextField(
        max_length=100
    )
    profileUrl = models.CharField(
        max_length=50
    )
    profileImage = models.CharField(
        max_length=50
    )
    age = models.DateTimeField(
        null=False, blank=False
    )
    isBanned = models.BooleanField(
        default=False, null=False, blank=False
    )


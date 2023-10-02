from django.db import models
import datetime
import uuid
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
    userId = models.UUIDField(
        blank=False,null=False, default=uuid.uuid4()
    )
    createdAt = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )
    updatedAt = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )
    status = models.TextField(
        max_length=100, default="offline"
    )
    profileUrl = models.CharField(
        max_length=50
    )
    profileImage = models.CharField(
        max_length=50
    )
    isBanned = models.BooleanField(
        default=False, null=False, blank=False
    )


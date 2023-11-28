from django.db import models
import datetime
# Create your models here.


class FriendList(models.Model):
    userId = models.UUIDField(
        blank=False, null=False
    )
    friendUI = models.UUIDField(
        blank=False, null=False
    )
    friendName = models.CharField(
        blank=False, null=False
    )
    friendsFrom = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )
    isBlock = models.BooleanField(
        default=False
    )

class MatchHistory(models.Model):
    matchId = models.UUIDField(
        blank=False, null=False
    )
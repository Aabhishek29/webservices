from django.db import models

# Create your models here.


class FeedBackClass(models.Model):
    name = models.CharField(
        max_length=30, blank=False, null=False
    )
    mail = models.EmailField(
        blank=False, null=False
    )
    subject = models.CharField(
        max_length=100, blank=True, null=True
    )
    msg = models.TextField(
        blank=False, null=False
    )
    fid = models.CharField(
        max_length=15, blank=False, null=False,
        primary_key=True
    )
    createdAt = models.DateTimeField(
        blank=False, null=False
    )

    def __str__(self) -> str:
        return super().__str__()
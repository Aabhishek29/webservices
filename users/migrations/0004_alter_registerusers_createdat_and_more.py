# Generated by Django 4.1.11 on 2023-10-03 16:34

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_registerusers_createdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerusers',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 22, 4, 55, 704984)),
        ),
        migrations.AlterField(
            model_name='registerusers',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 22, 4, 55, 704984)),
        ),
        migrations.AlterField(
            model_name='registerusers',
            name='userId',
            field=models.UUIDField(default=uuid.UUID('9a421a19-547c-4cf0-84ac-d07d65d3a44b'), unique=True),
        ),
    ]

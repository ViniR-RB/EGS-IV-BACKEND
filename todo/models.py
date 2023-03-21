import uuid

from django.db import models


# Create your models here.
class TodoModel(models.Model):
    id = models.AutoField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(
        max_length=80, blank=False, null=False)
    isCompleted = models.BooleanField(default=False, blank=False, null=False)

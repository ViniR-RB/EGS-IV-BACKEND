import uuid

from django.db import models


# Create your models here.
class TodoModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(
        max_length=80, blank=False, null=False)
    isCompleted = models.BooleanField(default=False, blank=False, null=False)

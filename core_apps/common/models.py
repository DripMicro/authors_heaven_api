import uuid 
from django.db import models


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at","-updated_at"]

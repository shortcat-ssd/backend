import secrets

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

def generate_id():
    return secrets.token_urlsafe(8)

class Short(models.Model):
    id = models.CharField(
        primary_key=True,
        unique=True,
        max_length=8,
        default=generate_id,
        validators=[MinLengthValidator(8)],
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField()
    private = models.BooleanField(default=False)

    stats = models.ForeignKey("ShortStats", on_delete=models.CASCADE)

    expired_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShortStats(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=8,
    )
    views = models.PositiveIntegerField(default=0)

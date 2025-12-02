import secrets

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


def generate_code(length: int = 8) -> str:
    return secrets.token_urlsafe(length)[:length]

class Short(models.Model):
    id = models.BigAutoField(primary_key=True)

    code = models.CharField(
        max_length=8,
        unique=True,
        default=generate_code,
        editable=False,
        validators=[MinLengthValidator(8)],
    )

    target = models.URLField()

    label = models.CharField(max_length=250, blank=True)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="shorts"
    )

    private = models.BooleanField(default=False)

    expired_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} -> {self.target}"

class ShortView(models.Model):
    short = models.ForeignKey(
        Short,
        on_delete=models.CASCADE,
        related_name="stats",
    )
    
    date = models.DateField(default=timezone.now)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short.code} | {self.date}"

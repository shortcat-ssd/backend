import secrets

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


def generate_code(length=8):
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
        related_name="shorts",
    )
    private = models.BooleanField(default=False)
    expired_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.code} -> {self.target}"

    @property
    def is_expired(self):
        if self.expired_at is None:
            return False
        return self.expired_at <= timezone.now()

class ShortView(models.Model):
    short = models.ForeignKey(
        Short,
        on_delete=models.CASCADE,
        related_name="views",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

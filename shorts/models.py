import secrets

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


def generate_code(length: int = 8) -> str:
    return secrets.token_urlsafe(length)


class Short(models.Model):
    id = models.BigAutoField(primary_key=True)

    code = models.CharField(
        max_length=20,  # for future-proofing
        unique=True,
        default=generate_code,
        editable=False,
    )

    target = models.URLField()

    label = models.CharField(max_length=250, blank=True)

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="shorts"
    )

    private = models.BooleanField(default=False)

    expired_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @staticmethod
    def get_readonly_fields():
        return ["id", "code", "created_at", "updated_at"]

    def __str__(self):
        return f"{self.code} -> {self.target}"


class ShortStats(models.Model):
    short = models.ForeignKey(
        Short,
        on_delete=models.CASCADE,
        related_name="stats",
    )

    date = models.DateField(default=timezone.now)
    ip = models.GenericIPAddressField(null=True, blank=True)

    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["short", "date", "ip"], name="uniq_short_date_ip"
            )
        ]

    def __str__(self):
        ip = self.ip or "unknown"
        return f"{self.short.code} | {self.date} | {ip} → {self.views} views"

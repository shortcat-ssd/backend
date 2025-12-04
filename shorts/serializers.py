import zoneinfo

from django.utils import timezone
from rest_framework import serializers

from shorts.models import Short, ShortClick


class ShortSerializer(serializers.ModelSerializer):
    expired_at = serializers.DateTimeField(
        required=False,
        allow_null=True,
        default_timezone=zoneinfo.ZoneInfo("Europe/Rome"),
    )

    class Meta:
        model = Short
        fields = (
            "code",
            "target",
            "label",
            "private",
            "expired_at",
            "created_at",
            "updated_at",
        )
        # immutable fields
        read_only_fields = ("user", "code")

    # automatic validation for expired_at field
    def validate_expired_at(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError("expiration date must be in the future")
        return value

    # automatic validation for target field
    def validate_target(self, value):
        if not value:
            raise serializers.ValidationError("target URL is required")
        return value


class ShortClicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortClick
        fields = ("created_at",)

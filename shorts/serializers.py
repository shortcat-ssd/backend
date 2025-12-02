from django.utils import timezone
from rest_framework import serializers

from shorts.models import Short, ShortView


class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Short
        fields = (
            "user",
            "code",
            "target",
            "label",
            "private",
            "expired_at",
            "created_at",
        )
        read_only_fields = ("user", "code", "created_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        if request:
            user = request.user
            is_owner = user.is_authenticated and instance.user == user
            is_staff = user.is_authenticated and user.is_staff
            if not (is_owner or is_staff):
                data.pop("user", None)
        return data

    def validate_expired_at(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError("Expiration date must be in the future.")
        return value

    def validate_target(self, value):
        if not value:
            raise serializers.ValidationError("Target URL is required.")
        return value


class ShortViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortView
        fields = ("created_at",)
        read_only_fields = ("created_at",)

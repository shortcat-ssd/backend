from rest_framework import serializers
from shorts.models import Short, ShortStats


class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Short
        fields = (
            "code",
            "target",
            "label",
            "private",
            "expire_at",
            "created_at",
        )


class ShortStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortStats
        fields = (
            "date",
            "views",
        )  # Expose only necessary fields for security and privacy reasons

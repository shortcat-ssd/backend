from rest_framework import serializers
from shorts.models import Short, ShortView


class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Short
        fields = (
            "code",
            "target",
            "label",
            "private",
            "expired_at",
            "created_at",
        )


class ShortViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortView
        fields = ("date",)

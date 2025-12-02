from rest_framework import serializers
from django.db.models import Sum
from shorts.models import Short, ShortStats


class ShortSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()
    
    class Meta:
        model = Short
        fields = (
            "code",
            "target",
            "label",
            "views",
            "private",
            "expired_at",
            "created_at",
        )
    
    def get_views(self, obj):
        return obj.stats.aggregate(total=Sum('views'))['total'] or 0


class ShortStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortStats
        fields = (
            "date",
            "views",
        )  # Expose only necessary fields for security and privacy reasons

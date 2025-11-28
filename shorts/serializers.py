from rest_framework import serializers
from shorts.models import Short, ShortStats

class ShortSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Short

class ShortStatsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ShortStats

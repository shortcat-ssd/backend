from rest_framework import generics, viewsets

from shorts.models import Short, ShortStats
from shorts.serializers import ShortSerializer, ShortStatsSerializer

class ShortViewSet(viewsets.ModelViewSet):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer

class ShortStatsViewSet(viewsets.ModelViewSet):
    queryset = ShortStats.objects.all()
    serializer_class = ShortStatsSerializer

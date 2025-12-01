from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404

from shorts.models import Short, ShortStats
from shorts.serializers import ShortSerializer, ShortStatsSerializer

class ShortViewSet(viewsets.ModelViewSet):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer

class ShortStatsViewSet(viewsets.ModelViewSet):
    queryset = ShortStats.objects.all()
    serializer_class = ShortStatsSerializer
    
    def get_queryset(self):
        short = get_object_or_404(Short, pk=self.kwargs['short_pk'])
        return ShortStats.objects.filter(short=short)
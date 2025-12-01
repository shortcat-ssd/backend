from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from shorts.models import Short, ShortStats
from shorts.serializers import ShortSerializer, ShortStatsSerializer


class ShortViewSet(viewsets.ModelViewSet):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer
    lookup_field = "code"


class ShortStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShortStats.objects.all()
    serializer_class = ShortStatsSerializer

    def get_queryset(self):
        short_code = self.kwargs.get("short_code")
        short = get_object_or_404(Short, code=short_code)
        return ShortStats.objects.filter(short=short)

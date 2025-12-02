from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from shorts.permissions import NotPrivate

from shorts.models import Short, ShortStats
from shorts.serializers import ShortSerializer, ShortStatsSerializer

class ShortViewSet(viewsets.ModelViewSet):
    permission_classes = [NotPrivate]
    queryset = Short.objects.all()
    serializer_class = ShortSerializer
    lookup_field = "code"
        
class ShortStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShortStats.objects.all()
    serializer_class = ShortStatsSerializer

    def get_queryset(self):
        code = self.kwargs.get("short_code")
        short = get_object_or_404(Short, code=code)
        if short.user != self.request.user:
            raise PermissionDenied()
        return ShortStats.objects.filter(short=short)

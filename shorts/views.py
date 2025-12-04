from django.http import Http404
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from shorts.permissions import IsOwner
from shorts.exceptions import NotFound
from shorts.models import Short, ShortClick
from shorts.serializers import ShortSerializer, ShortClicksSerializer


class ShortsListView(generics.ListCreateAPIView):
    """
    List all shorts for the authenticated user or create a new short.
    """

    serializer_class = ShortSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Short.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ShortDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a short by its code.
    """

    serializer_class = ShortSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = "code"

    def get_object(self):
        try:
            return super().get_object()
        except (NotAuthenticated, PermissionDenied, Http404):
            # Raise 404 to prevent leakage.
            # We catch Http404 too, to override error messages
            raise NotFound

    def get_queryset(self):
        code = self.kwargs.get("code")
        return Short.objects.filter(code=code)


class ShortClicksView(generics.ListAPIView):
    """
    List all clicks for a specific short by its code.
    """

    serializer_class = ShortClicksSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = "code"

    def get_queryset(self):
        code = self.kwargs.get("code")
        try:
            short = Short.objects.get(code=code)
            self.check_object_permissions(self.request, short)
        except (NotAuthenticated, PermissionDenied, Short.DoesNotExist):
            raise NotFound
        return ShortClick.objects.filter(short=short)

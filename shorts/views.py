from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from shorts.models import Short, ShortView
from shorts.serializers import ShortSerializer, ShortViewSerializer
from shorts.permissions import IsOwnerOrReadOnly, IsPublicOrOwner

class ShortList(generics.ListCreateAPIView):
    serializer_class = ShortSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Short.objects.all()
        return Short.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShortDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShortSerializer
    lookup_field = "code"

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsPublicOrOwner()]
        return [IsAuthenticated(), IsOwnerOrReadOnly()]

    def get_queryset(self):
        return Short.objects.all()

class ShortViewsList(generics.ListAPIView):
    serializer_class = ShortViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        code = self.kwargs.get("code")
        queryset = Short.objects.filter(code=code)
        if not user.is_staff:
            queryset = queryset.filter(user=user)
        short = get_object_or_404(queryset)
        return ShortView.objects.filter(short=short)


def redirect_short(request, code):
    short = get_object_or_404(Short, code=code)
    if short.is_expired:
        raise Http404
    if short.private and (not request.user.is_authenticated or request.user != short.user):
        raise Http404
    ShortView.objects.create(short=short)
    return redirect(short.target)
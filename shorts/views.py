from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from shorts.permissions import CanViewOrEdit
from rest_framework.permissions import IsAdminUser

from shorts.models import Short, ShortView
from shorts.serializers import ShortSerializer, ShortViewSerializer

class ShortList(generics.ListCreateAPIView):
    queryset = Short.objects.all()
    serializer_class = ShortSerializer

    def get_queryset(self):
        return Short.objects.filter(user=self.request.user)

class ShortDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CanViewOrEdit | IsAdminUser]
    queryset = Short.objects.all()
    serializer_class = ShortSerializer
    lookup_field = "code"

class ShortViewsList(generics.ListAPIView):
    queryset = ShortView.objects.all()
    serializer_class = ShortViewSerializer

    def get_queryset(self):
        from_user = self.request.user
        code = self.kwargs.get("code")
        short = get_object_or_404(Short, code=code)
        if not from_user.is_staff and short.user != from_user:
            raise PermissionDenied()
        return ShortView.objects.filter(short=short)

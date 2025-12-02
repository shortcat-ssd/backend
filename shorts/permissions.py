from rest_framework.permissions import BasePermission
from rest_framework import permissions
    
class CanViewOrEdit(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.user == request.user:
                return True
            return obj.private is False
        return obj.user == request.user
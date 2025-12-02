from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsPublicOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.private:
            if not request.user.is_authenticated:
                return False
            return obj.user == request.user or request.user.is_staff
        return True
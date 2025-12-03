from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnlyIfPublic(BasePermission):
    """
    Custom permission to only allow read-only access to public shorts.
    For private shorts, only the owner (and superusers) can access.
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True
        if obj.private:
            return obj.user == request.user
        if request.method in SAFE_METHODS:
            return True
        return False


class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True
        return obj.user == request.user

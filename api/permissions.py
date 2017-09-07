from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser
from .serializers import PostOpenDataSerializer


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or obj.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAuthOrBlockData(permissions.BasePermission):
    """
    Custom permission to only allow open data for anonymous user.
    """
    def has_object_permission(self, request, view, obj):
        if type(request.user) == AnonymousUser:
            view.serializer_class = PostOpenDataSerializer
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


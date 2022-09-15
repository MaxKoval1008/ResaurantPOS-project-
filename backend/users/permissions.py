from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.email == request.user.email


class CanGetListUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'list' and (request.user.is_admin or request.user.is_superuser):
            return True

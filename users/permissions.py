from rest_framework import permissions


class CustomUserPermissions(permissions.BasePermission):
    """
    Permission ensures that all User related endpoints
    need authentication but the one for registration.
    Also prevents User from being able to update the profile
    for another account.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True

        return view.action == 'create'

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update'] and obj != request.user:
            return False

        return True

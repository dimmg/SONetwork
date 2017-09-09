from rest_framework import permissions


class IsOwnerOnNonSafeMethods(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy'] and obj.author != request.user:
            return False

        return True

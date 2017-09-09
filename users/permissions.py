from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return True

        return view.action == 'create'

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update'] and obj != request.user:
            return False

        return True

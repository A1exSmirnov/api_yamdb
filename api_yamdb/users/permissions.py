from rest_framework import permissions


class IsAdministrator(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_administrator or request.user.is_superuser
        )

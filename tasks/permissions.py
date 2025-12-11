from rest_framework import permissions
class IsAdminOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return True


    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
             return True
        return getattr(obj, 'owner', None) == request.user
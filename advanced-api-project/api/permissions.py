from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions for safe methods (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object
        return obj.added_by == request.user
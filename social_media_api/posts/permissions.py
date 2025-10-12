from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow owners of an object to edit it; others only read."""
def has_object_permission(self, request, view, obj):
    # Read permissions are allowed to any request
    if request.method in permissions.SAFE_METHODS:
        return True
# Write permissions only to owner
    try:
        return obj.author == request.user
    except AttributeError:
        return False
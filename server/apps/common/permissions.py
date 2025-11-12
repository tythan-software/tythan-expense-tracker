from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access.
    """

    message = "You do not have permission to access or modify."

    def has_object_permission(self, request, view, obj):
        # If the request method is not safe, only allow the request if the user making the request is the owner of the object.
        return obj.owner == request.user
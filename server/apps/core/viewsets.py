from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from apps.common.permissions import IsOwnerOnly


class AuthViewSet(ViewSet):
    """
    Auth ViewSet for all APIs.
    Handles common permission logic.
    """

    # Default global permissions for each CRUD action
    default_permission_classes_by_action = {
        "list": [IsAuthenticated, IsOwnerOnly],
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwnerOnly],
        "destroy": [IsAuthenticated, IsOwnerOnly],
    }

    def get_permissions(self):
        """
        Dynamically choose permission classes based on the action.
        Allows child ViewSets to override or extend via `permission_classes_by_action`.
        """
        # Start from the base mapping
        permission_classes_by_action = dict(self.default_permission_classes_by_action)

        # Allow subclasses to add or override
        if hasattr(self, "permission_classes_by_action"):
            permission_classes_by_action.update(self.permission_classes_by_action)

        # Select permissions for this action (fallback to IsAuthenticated)
        permission_classes = permission_classes_by_action.get(
            self.action, [IsAuthenticated]
        )

        return [permission() for permission in permission_classes]

# permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # allow read only requests
        return request.user.is_staff or obj.author_id == request.user.id  # allow owner or admin to modify
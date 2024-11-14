from rest_framework.permissions import BasePermission
from rest_framework import permissions

from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to restrict access to tasks:
    - Anyone can view tasks (GET requests).
    - Only authenticated users can modify tasks (POST, PUT, DELETE requests).
    - Super admins can access all tasks.
    - Normal users can only access their own tasks.
    """

    def has_permission(self, request, view):
        # Allow anyone to view tasks (GET requests)
        if request.method == 'GET':
            return True
        
        # Only allow authenticated users for non-GET requests
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Superadmins can access all tasks
        if request.user.is_superuser:
            return True
        
        # Normal users can only access their own tasks
        return obj.owner == request.user

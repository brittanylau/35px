from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a photo/comment to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the photo/comment.
        return obj.author.user == request.user

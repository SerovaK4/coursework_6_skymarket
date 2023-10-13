# TODO здесь производится настройка пермишенов для нашего проекта

from rest_framework import permissions

from skymarket.users.models import User


class ReadOrCreatePermission(permissions.BasePermission):
    message = 'This operation is available only to Authorized users'

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        else:
            if not request.user.is_authenticated:
                return False
            else:
                if view.action in ['retrieve', 'create', 'me']:
                    return True
                else:
                    if request.user.role == User.ADMIN:
                        return True


class OwnerOrAdminPermission(permissions.BasePermission):
    message = 'This operation is available only to Owner or Admin.'

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.role == User.ADMIN:
            return True
        if obj.__class__ == "User":
            owner = obj
        else:
            owner = obj.author
        return request.user.is_authenticated and owner == request.user
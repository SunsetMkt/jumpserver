# -*- coding: utf-8 -*-
#
from rest_framework.request import Request

from common.http import is_true
from common.mixins.api import RoleAdminMixin
from common.mixins.api import RoleUserMixin
from orgs.utils import tmp_to_root_org
from users.models import User
from perms.utils.user_permission import UserGrantedTreeRefreshController


class RebuildTreeMixin:
    user: User

    def get(self, request: Request, *args, **kwargs):
        force = is_true(request.query_params.get('rebuild_tree'))
        controller = UserGrantedTreeRefreshController(self.user)
        controller.refresh_if_need(force)
        return super().get(request, *args, **kwargs)


class AssetRoleAdminMixin(RebuildTreeMixin, RoleAdminMixin):
    rbac_perms = (
        ('list', 'perms.view_userassets'),
        ('retrieve', 'perms.view_userassets'),
        ('get_tree', 'perms.view_userassets'),
        ('GET', 'perms.view_userassets'),
    )


class AssetRoleUserMixin(RebuildTreeMixin, RoleUserMixin):
    rbac_perms = (
        ('list', 'perms.view_myassets'),
        ('retrieve', 'perms.view_myassets'),
        ('get_tree', 'perms.view_myassets'),
        ('GET', 'perms.view_myassets'),
    )
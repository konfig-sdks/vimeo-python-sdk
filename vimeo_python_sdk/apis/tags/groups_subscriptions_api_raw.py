# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_groups_group_id.put import AddUserToGroupRaw
from vimeo_python_sdk.paths.users_user_id_groups_group_id.put import GroupRaw
from vimeo_python_sdk.paths.users_user_id_groups_group_id.delete import Group0Raw
from vimeo_python_sdk.paths.me_groups_group_id.delete import RemoveUserFromGroupRaw


class GroupsSubscriptionsApiRaw(
    AddUserToGroupRaw,
    GroupRaw,
    Group0Raw,
    RemoveUserFromGroupRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
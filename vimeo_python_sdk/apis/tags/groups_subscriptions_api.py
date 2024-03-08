# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.me_groups_group_id.put import AddUserToGroup
from vimeo_python_sdk.paths.users_user_id_groups_group_id.put import Group
from vimeo_python_sdk.paths.users_user_id_groups_group_id.delete import Group0
from vimeo_python_sdk.paths.me_groups_group_id.delete import RemoveUserFromGroup
from vimeo_python_sdk.apis.tags.groups_subscriptions_api_raw import GroupsSubscriptionsApiRaw


class GroupsSubscriptionsApi(
    AddUserToGroup,
    Group,
    Group0,
    RemoveUserFromGroup,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GroupsSubscriptionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GroupsSubscriptionsApiRaw(api_client)

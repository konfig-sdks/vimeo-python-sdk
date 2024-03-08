# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from vimeo_python_sdk.paths.teammembers_code.get import GetMembershipInformation
from vimeo_python_sdk.paths.users_user_id_team_users_team_user_id.get import GetTeamMembershipInformation
from vimeo_python_sdk.paths.users_user_id_team_role.get import GetUserTeamRole
from vimeo_python_sdk.apis.tags.teams_members_api_raw import TeamsMembersApiRaw


class TeamsMembersApi(
    GetMembershipInformation,
    GetTeamMembershipInformation,
    GetUserTeamRole,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TeamsMembersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TeamsMembersApiRaw(api_client)
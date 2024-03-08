# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from vimeo_python_sdk.type.team_role_applicable_permission_policies import TeamRoleApplicablePermissionPolicies

class RequiredTeamRole(TypedDict):
    # The untranslated role of the user who made the request.  Option descriptions:  * `Admin` - The team member has admin permissions. They can upload and edit videos for the entire team and perform team administration tasks.  * `Contributor` - The team member has contributor permissions. They can upload and edit videos for the entire team but can’t perform team administration tasks.  * `Contributor Plus` - The team member has contributor-plus permissions. They can upload and edit videos for the entire team and have additional sets of permissions but can't perform team administration tasks.  * `Owner` - The team member has owner permissions.  * `Uploader` - The team member has uploader permissions. They can upload videos for the entire team but can't edit videos.  * `Viewer` - The team member has viewer permissions. They can access team videos and specific team folders but can't upload or edit videos. 
    permission_level: typing.Optional[str]

    # The untranslated role of the user who made the request.  Option descriptions:  * `Admin` - The team member has admin permissions. They can upload and edit videos for the entire team and perform team administration tasks.  * `Contributor` - The team member has contributor permissions. They can upload and edit videos for the entire team but can’t perform team administration tasks.  * `Contributor Plus` - The team member has contributor-plus permissions. They can upload and edit videos for the entire team and have additional sets of permissions but can't perform team administration tasks.  * `Owner` - The team member has owner permissions.  * `Uploader` - The team member has uploader permissions. They can upload videos for the entire team but can’t edit videos.  * `Viewer` - The team member has viewer permissions. They can access team videos and specific team folders but can’t upload or edit videos. 
    role: typing.Optional[str]

    # The unique identifier to access the team role.
    uri: str

class OptionalTeamRole(TypedDict, total=False):
    applicable_permission_policies: TeamRoleApplicablePermissionPolicies

    # The total number of team members with this role.
    count: typing.Union[int, float]

    # The translated display description of the role.
    display_description: str

    # The translated display name of the role.
    display_name: str

class TeamRole(RequiredTeamRole, OptionalTeamRole):
    pass

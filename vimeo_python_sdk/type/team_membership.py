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

from vimeo_python_sdk.type.team_membership_applicable_permission_policies import TeamMembershipApplicablePermissionPolicies
from vimeo_python_sdk.type.team_membership_metadata import TeamMembershipMetadata
from vimeo_python_sdk.type.team_role import TeamRole
from vimeo_python_sdk.type.user import User

class RequiredTeamMembership(TypedDict):
    # Information about an access grant that applies to the team member on the folder. _This field is deprecated because grants are no longer exposed via API responses._
    access_grant: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # Whether the team membership is currently active.
    active: bool

    applicable_permission_policies: TeamMembershipApplicablePermissionPolicies

    # An array of the team roles this team member can have.
    applicable_roles: typing.List[TeamRole]

    # The time in ISO 8601 format when the invite was sent.
    created_time: str

    # The team member's email.
    email: str

    # The URL for the invited user to join the team. The value of this field is null if the invited user has already joined.
    invite_url: typing.Optional[str]

    # The time in ISO 8601 format when the invite was accepted.
    joined_time: str

    metadata: TeamMembershipMetadata

    # The time in ISO 8601 format when the team membership was last modified.
    modified_time: str

    # The team member's permission level.  Option descriptions:  * `Admin` - The team member has admin permissions. They can upload and edit videos for the entire team and perform team administration tasks.  * `Contributor` - The team member has contributor permissions. They can upload and edit videos for the entire team but can't perform team administration tasks.  * `Contributor Plus` - The team member has contributor plus permissions. They can upload and edit videos for the entire team, and have additional sets of permissions, but can't perform team administration tasks.  * `Owner` - The team member has owner permissions.  * `Uploader` - The team member has uploader permissions. They can upload videos for the entire team but can't edit videos.  * `Viewer` - The team member has viewer permissions. They can access team videos and specific team folders but can't upload or edit videos. 
    permission_level: str

    # The resource key of the team membership.
    resource_key: str

    # The team member's role, translated.
    role: str

    # The status of the team membership invite.  Option descriptions:  * `accepted` - Team membership has been accepted.  * `pending` - Team membership has been offered but not yet accepted. 
    status: str

    # The unique identifier to access the team membership resource.
    uri: str

    # The team member. The value of this field is null if the user hasn't joined the team yet.
    user: User

class OptionalTeamMembership(TypedDict, total=False):
    # Whether the team member has folder access.
    has_folder_access: bool

    # Whether the team member has been reminded about the invite.
    recently_reminded: bool

class TeamMembership(RequiredTeamMembership, OptionalTeamMembership):
    pass

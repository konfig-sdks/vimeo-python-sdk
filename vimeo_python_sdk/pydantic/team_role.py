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
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.team_role_applicable_permission_policies import TeamRoleApplicablePermissionPolicies

class TeamRole(BaseModel):
    # The untranslated role of the user who made the request.  Option descriptions:  * `Admin` - The team member has admin permissions. They can upload and edit videos for the entire team and perform team administration tasks.  * `Contributor` - The team member has contributor permissions. They can upload and edit videos for the entire team but can’t perform team administration tasks.  * `Contributor Plus` - The team member has contributor-plus permissions. They can upload and edit videos for the entire team and have additional sets of permissions but can't perform team administration tasks.  * `Owner` - The team member has owner permissions.  * `Uploader` - The team member has uploader permissions. They can upload videos for the entire team but can't edit videos.  * `Viewer` - The team member has viewer permissions. They can access team videos and specific team folders but can't upload or edit videos. 
    permission_level: Literal["Admin", "Contributor", "Contributor Plus", "Owner", "Uploader", "Viewer"] = Field(alias='permission_level')

    # The untranslated role of the user who made the request.  Option descriptions:  * `Admin` - The team member has admin permissions. They can upload and edit videos for the entire team and perform team administration tasks.  * `Contributor` - The team member has contributor permissions. They can upload and edit videos for the entire team but can’t perform team administration tasks.  * `Contributor Plus` - The team member has contributor-plus permissions. They can upload and edit videos for the entire team and have additional sets of permissions but can't perform team administration tasks.  * `Owner` - The team member has owner permissions.  * `Uploader` - The team member has uploader permissions. They can upload videos for the entire team but can’t edit videos.  * `Viewer` - The team member has viewer permissions. They can access team videos and specific team folders but can’t upload or edit videos. 
    role: Literal["Admin", "Contributor", "Contributor Plus", "Owner", "Uploader", "Viewer"] = Field(alias='role')

    # The unique identifier to access the team role.
    uri: str = Field(alias='uri')

    applicable_permission_policies: typing.Optional[TeamRoleApplicablePermissionPolicies] = Field(None, alias='applicable_permission_policies')

    # The total number of team members with this role.
    count: typing.Optional[typing.Union[int, float]] = Field(None, alias='count')

    # The translated display description of the role.
    display_description: typing.Optional[str] = Field(None, alias='display_description')

    # The translated display name of the role.
    display_name: typing.Optional[str] = Field(None, alias='display_name')
    class Config:
        arbitrary_types_allowed = True

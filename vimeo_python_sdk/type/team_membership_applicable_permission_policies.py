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

from vimeo_python_sdk.type.permission_policy import PermissionPolicy

class RequiredTeamMembershipApplicablePermissionPolicies(TypedDict):
    # An array of folder permission policies that can apply to the team member.
    folder: typing.List[PermissionPolicy]

    # An array of regional delivery permission policies that can apply to the team member.
    regional_delivery: typing.List[PermissionPolicy]

    # An array of video permission policies that can apply to the team member.
    video: typing.List[PermissionPolicy]

class OptionalTeamMembershipApplicablePermissionPolicies(TypedDict, total=False):
    pass

class TeamMembershipApplicablePermissionPolicies(RequiredTeamMembershipApplicablePermissionPolicies, OptionalTeamMembershipApplicablePermissionPolicies):
    pass

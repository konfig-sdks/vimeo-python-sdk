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

from vimeo_python_sdk.type.team_role_applicable_permission_policies_folder import TeamRoleApplicablePermissionPoliciesFolder
from vimeo_python_sdk.type.team_role_applicable_permission_policies_regional_delivery import TeamRoleApplicablePermissionPoliciesRegionalDelivery
from vimeo_python_sdk.type.team_role_applicable_permission_policies_video import TeamRoleApplicablePermissionPoliciesVideo

class RequiredTeamRoleApplicablePermissionPolicies(TypedDict):
    pass

class OptionalTeamRoleApplicablePermissionPolicies(TypedDict, total=False):
    folder: TeamRoleApplicablePermissionPoliciesFolder

    regional_delivery: TeamRoleApplicablePermissionPoliciesRegionalDelivery

    video: TeamRoleApplicablePermissionPoliciesVideo

class TeamRoleApplicablePermissionPolicies(RequiredTeamRoleApplicablePermissionPolicies, OptionalTeamRoleApplicablePermissionPolicies):
    pass

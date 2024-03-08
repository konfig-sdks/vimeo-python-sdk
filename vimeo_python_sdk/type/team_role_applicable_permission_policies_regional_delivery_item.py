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


class RequiredTeamRoleApplicablePermissionPoliciesRegionalDeliveryItem(TypedDict):
    # The translated display description of the regional delivery permission policy.
    display_description: str

    # The translated display name of the regional delivery permission policy.
    display_name: str

    # The name of the regional delivery permission policy.
    name: str

class OptionalTeamRoleApplicablePermissionPoliciesRegionalDeliveryItem(TypedDict, total=False):
    pass

class TeamRoleApplicablePermissionPoliciesRegionalDeliveryItem(RequiredTeamRoleApplicablePermissionPoliciesRegionalDeliveryItem, OptionalTeamRoleApplicablePermissionPoliciesRegionalDeliveryItem):
    pass

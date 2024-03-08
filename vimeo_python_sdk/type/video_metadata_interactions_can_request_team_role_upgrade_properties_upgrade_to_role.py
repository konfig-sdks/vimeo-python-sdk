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


class RequiredVideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole(TypedDict):
    # Whether the upgrade role must be sent to achieve the desired action.
    required: bool

    # The value of the team role to which the user should be upgraded.
    value: typing.Union[int, float]

class OptionalVideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole(TypedDict, total=False):
    pass

class VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole(RequiredVideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole, OptionalVideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole):
    pass

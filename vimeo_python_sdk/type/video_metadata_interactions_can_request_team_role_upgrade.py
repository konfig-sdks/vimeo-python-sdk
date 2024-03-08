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

from vimeo_python_sdk.type.video_metadata_interactions_can_request_team_role_upgrade_options import VideoMetadataInteractionsCanRequestTeamRoleUpgradeOptions
from vimeo_python_sdk.type.video_metadata_interactions_can_request_team_role_upgrade_properties import VideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties

class RequiredVideoMetadataInteractionsCanRequestTeamRoleUpgrade(TypedDict):
    options: VideoMetadataInteractionsCanRequestTeamRoleUpgradeOptions

    properties: VideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsCanRequestTeamRoleUpgrade(TypedDict, total=False):
    pass

class VideoMetadataInteractionsCanRequestTeamRoleUpgrade(RequiredVideoMetadataInteractionsCanRequestTeamRoleUpgrade, OptionalVideoMetadataInteractionsCanRequestTeamRoleUpgrade):
    pass

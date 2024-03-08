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

from vimeo_python_sdk.type.video_metadata_interactions_can_request_team_role_upgrade_properties_folder_uri import VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesFolderUri
from vimeo_python_sdk.type.video_metadata_interactions_can_request_team_role_upgrade_properties_status import VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesStatus
from vimeo_python_sdk.type.video_metadata_interactions_can_request_team_role_upgrade_properties_upgrade_to_role import VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole

class RequiredVideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties(TypedDict):
    folder_uri: VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesFolderUri

    status: VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesStatus

    upgrade_to_role: VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesUpgradeToRole

class OptionalVideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties(TypedDict, total=False):
    pass

class VideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties(RequiredVideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties, OptionalVideoMetadataInteractionsCanRequestTeamRoleUpgradeProperties):
    pass

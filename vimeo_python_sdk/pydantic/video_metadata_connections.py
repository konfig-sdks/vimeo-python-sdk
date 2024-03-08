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

from vimeo_python_sdk.pydantic.ancestor_path import AncestorPath
from vimeo_python_sdk.pydantic.video_metadata_connections_available_channels import VideoMetadataConnectionsAvailableChannels
from vimeo_python_sdk.pydantic.video_metadata_connections_comments import VideoMetadataConnectionsComments
from vimeo_python_sdk.pydantic.video_metadata_connections_credits import VideoMetadataConnectionsCredits
from vimeo_python_sdk.pydantic.video_metadata_connections_likes import VideoMetadataConnectionsLikes
from vimeo_python_sdk.pydantic.video_metadata_connections_ondemand import VideoMetadataConnectionsOndemand
from vimeo_python_sdk.pydantic.video_metadata_connections_pictures import VideoMetadataConnectionsPictures
from vimeo_python_sdk.pydantic.video_metadata_connections_recommendations import VideoMetadataConnectionsRecommendations
from vimeo_python_sdk.pydantic.video_metadata_connections_related import VideoMetadataConnectionsRelated
from vimeo_python_sdk.pydantic.video_metadata_connections_resource_creator_team_user import VideoMetadataConnectionsResourceCreatorTeamUser
from vimeo_python_sdk.pydantic.video_metadata_connections_season import VideoMetadataConnectionsSeason
from vimeo_python_sdk.pydantic.video_metadata_connections_team_permissions import VideoMetadataConnectionsTeamPermissions
from vimeo_python_sdk.pydantic.video_metadata_connections_texttracks import VideoMetadataConnectionsTexttracks
from vimeo_python_sdk.pydantic.video_metadata_connections_trailer import VideoMetadataConnectionsTrailer
from vimeo_python_sdk.pydantic.video_metadata_connections_users_with_access import VideoMetadataConnectionsUsersWithAccess
from vimeo_python_sdk.pydantic.video_metadata_connections_versions import VideoMetadataConnectionsVersions

class VideoMetadataConnections(BaseModel):
    # Information about the video's ancestry, ordered from the direct parent folder to higher-level ancestors.
    ancestor_path: typing.List[AncestorPath] = Field(alias='ancestor_path')

    available_channels: VideoMetadataConnectionsAvailableChannels = Field(alias='available_channels')

    comments: VideoMetadataConnectionsComments = Field(alias='comments')

    credits: VideoMetadataConnectionsCredits = Field(alias='credits')

    likes: VideoMetadataConnectionsLikes = Field(alias='likes')

    ondemand: VideoMetadataConnectionsOndemand = Field(alias='ondemand')

    pictures: VideoMetadataConnectionsPictures = Field(alias='pictures')

    recommendations: VideoMetadataConnectionsRecommendations = Field(alias='recommendations')

    related: VideoMetadataConnectionsRelated = Field(alias='related')

    resource_creator_team_user: VideoMetadataConnectionsResourceCreatorTeamUser = Field(alias='resource_creator_team_user')

    season: VideoMetadataConnectionsSeason = Field(alias='season')

    team_permissions: VideoMetadataConnectionsTeamPermissions = Field(alias='team_permissions')

    texttracks: VideoMetadataConnectionsTexttracks = Field(alias='texttracks')

    trailer: VideoMetadataConnectionsTrailer = Field(alias='trailer')

    users_with_access: VideoMetadataConnectionsUsersWithAccess = Field(alias='users_with_access')

    versions: VideoMetadataConnectionsVersions = Field(alias='versions')
    class Config:
        arbitrary_types_allowed = True

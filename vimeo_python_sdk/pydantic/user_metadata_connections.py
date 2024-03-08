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

from vimeo_python_sdk.pydantic.user_metadata_connections_albums import UserMetadataConnectionsAlbums
from vimeo_python_sdk.pydantic.user_metadata_connections_appearances import UserMetadataConnectionsAppearances
from vimeo_python_sdk.pydantic.user_metadata_connections_block import UserMetadataConnectionsBlock
from vimeo_python_sdk.pydantic.user_metadata_connections_categories import UserMetadataConnectionsCategories
from vimeo_python_sdk.pydantic.user_metadata_connections_channels import UserMetadataConnectionsChannels
from vimeo_python_sdk.pydantic.user_metadata_connections_connected_apps import UserMetadataConnectionsConnectedApps
from vimeo_python_sdk.pydantic.user_metadata_connections_feed import UserMetadataConnectionsFeed
from vimeo_python_sdk.pydantic.user_metadata_connections_folders import UserMetadataConnectionsFolders
from vimeo_python_sdk.pydantic.user_metadata_connections_folders_root import UserMetadataConnectionsFoldersRoot
from vimeo_python_sdk.pydantic.user_metadata_connections_followers import UserMetadataConnectionsFollowers
from vimeo_python_sdk.pydantic.user_metadata_connections_following import UserMetadataConnectionsFollowing
from vimeo_python_sdk.pydantic.user_metadata_connections_groups import UserMetadataConnectionsGroups
from vimeo_python_sdk.pydantic.user_metadata_connections_likes import UserMetadataConnectionsLikes
from vimeo_python_sdk.pydantic.user_metadata_connections_moderated_channels import UserMetadataConnectionsModeratedChannels
from vimeo_python_sdk.pydantic.user_metadata_connections_pictures import UserMetadataConnectionsPictures
from vimeo_python_sdk.pydantic.user_metadata_connections_portfolios import UserMetadataConnectionsPortfolios
from vimeo_python_sdk.pydantic.user_metadata_connections_recommended_channels import UserMetadataConnectionsRecommendedChannels
from vimeo_python_sdk.pydantic.user_metadata_connections_recommended_users import UserMetadataConnectionsRecommendedUsers
from vimeo_python_sdk.pydantic.user_metadata_connections_shared import UserMetadataConnectionsShared
from vimeo_python_sdk.pydantic.user_metadata_connections_videos import UserMetadataConnectionsVideos
from vimeo_python_sdk.pydantic.user_metadata_connections_watched_videos import UserMetadataConnectionsWatchedVideos
from vimeo_python_sdk.pydantic.user_metadata_connections_watchlater import UserMetadataConnectionsWatchlater

class UserMetadataConnections(BaseModel):
    albums: UserMetadataConnectionsAlbums = Field(alias='albums')

    appearances: UserMetadataConnectionsAppearances = Field(alias='appearances')

    block: UserMetadataConnectionsBlock = Field(alias='block')

    categories: UserMetadataConnectionsCategories = Field(alias='categories')

    channels: UserMetadataConnectionsChannels = Field(alias='channels')

    connected_apps: UserMetadataConnectionsConnectedApps = Field(alias='connected_apps')

    feed: UserMetadataConnectionsFeed = Field(alias='feed')

    folders: UserMetadataConnectionsFolders = Field(alias='folders')

    folders_root: UserMetadataConnectionsFoldersRoot = Field(alias='folders_root')

    followers: UserMetadataConnectionsFollowers = Field(alias='followers')

    following: UserMetadataConnectionsFollowing = Field(alias='following')

    groups: UserMetadataConnectionsGroups = Field(alias='groups')

    likes: UserMetadataConnectionsLikes = Field(alias='likes')

    moderated_channels: UserMetadataConnectionsModeratedChannels = Field(alias='moderated_channels')

    pictures: UserMetadataConnectionsPictures = Field(alias='pictures')

    portfolios: UserMetadataConnectionsPortfolios = Field(alias='portfolios')

    recommended_channels: UserMetadataConnectionsRecommendedChannels = Field(alias='recommended_channels')

    recommended_users: UserMetadataConnectionsRecommendedUsers = Field(alias='recommended_users')

    shared: UserMetadataConnectionsShared = Field(alias='shared')

    videos: UserMetadataConnectionsVideos = Field(alias='videos')

    watched_videos: UserMetadataConnectionsWatchedVideos = Field(alias='watched_videos')

    watchlater: UserMetadataConnectionsWatchlater = Field(alias='watchlater')
    class Config:
        arbitrary_types_allowed = True

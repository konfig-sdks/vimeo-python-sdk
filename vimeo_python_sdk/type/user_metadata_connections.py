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

from vimeo_python_sdk.type.user_metadata_connections_albums import UserMetadataConnectionsAlbums
from vimeo_python_sdk.type.user_metadata_connections_appearances import UserMetadataConnectionsAppearances
from vimeo_python_sdk.type.user_metadata_connections_block import UserMetadataConnectionsBlock
from vimeo_python_sdk.type.user_metadata_connections_categories import UserMetadataConnectionsCategories
from vimeo_python_sdk.type.user_metadata_connections_channels import UserMetadataConnectionsChannels
from vimeo_python_sdk.type.user_metadata_connections_connected_apps import UserMetadataConnectionsConnectedApps
from vimeo_python_sdk.type.user_metadata_connections_feed import UserMetadataConnectionsFeed
from vimeo_python_sdk.type.user_metadata_connections_folders import UserMetadataConnectionsFolders
from vimeo_python_sdk.type.user_metadata_connections_folders_root import UserMetadataConnectionsFoldersRoot
from vimeo_python_sdk.type.user_metadata_connections_followers import UserMetadataConnectionsFollowers
from vimeo_python_sdk.type.user_metadata_connections_following import UserMetadataConnectionsFollowing
from vimeo_python_sdk.type.user_metadata_connections_groups import UserMetadataConnectionsGroups
from vimeo_python_sdk.type.user_metadata_connections_likes import UserMetadataConnectionsLikes
from vimeo_python_sdk.type.user_metadata_connections_moderated_channels import UserMetadataConnectionsModeratedChannels
from vimeo_python_sdk.type.user_metadata_connections_pictures import UserMetadataConnectionsPictures
from vimeo_python_sdk.type.user_metadata_connections_portfolios import UserMetadataConnectionsPortfolios
from vimeo_python_sdk.type.user_metadata_connections_recommended_channels import UserMetadataConnectionsRecommendedChannels
from vimeo_python_sdk.type.user_metadata_connections_recommended_users import UserMetadataConnectionsRecommendedUsers
from vimeo_python_sdk.type.user_metadata_connections_shared import UserMetadataConnectionsShared
from vimeo_python_sdk.type.user_metadata_connections_videos import UserMetadataConnectionsVideos
from vimeo_python_sdk.type.user_metadata_connections_watched_videos import UserMetadataConnectionsWatchedVideos
from vimeo_python_sdk.type.user_metadata_connections_watchlater import UserMetadataConnectionsWatchlater

class RequiredUserMetadataConnections(TypedDict):
    albums: UserMetadataConnectionsAlbums

    appearances: UserMetadataConnectionsAppearances

    block: UserMetadataConnectionsBlock

    categories: UserMetadataConnectionsCategories

    channels: UserMetadataConnectionsChannels

    connected_apps: UserMetadataConnectionsConnectedApps

    feed: UserMetadataConnectionsFeed

    folders: UserMetadataConnectionsFolders

    folders_root: UserMetadataConnectionsFoldersRoot

    followers: UserMetadataConnectionsFollowers

    following: UserMetadataConnectionsFollowing

    groups: UserMetadataConnectionsGroups

    likes: UserMetadataConnectionsLikes

    moderated_channels: UserMetadataConnectionsModeratedChannels

    pictures: UserMetadataConnectionsPictures

    portfolios: UserMetadataConnectionsPortfolios

    recommended_channels: UserMetadataConnectionsRecommendedChannels

    recommended_users: UserMetadataConnectionsRecommendedUsers

    shared: UserMetadataConnectionsShared

    videos: UserMetadataConnectionsVideos

    watched_videos: UserMetadataConnectionsWatchedVideos

    watchlater: UserMetadataConnectionsWatchlater

class OptionalUserMetadataConnections(TypedDict, total=False):
    pass

class UserMetadataConnections(RequiredUserMetadataConnections, OptionalUserMetadataConnections):
    pass

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

from vimeo_python_sdk.type.album_metadata_interactions_add_custom_thumbnails import AlbumMetadataInteractionsAddCustomThumbnails
from vimeo_python_sdk.type.album_metadata_interactions_add_live_events import AlbumMetadataInteractionsAddLiveEvents
from vimeo_python_sdk.type.album_metadata_interactions_add_logos import AlbumMetadataInteractionsAddLogos
from vimeo_python_sdk.type.album_metadata_interactions_add_to import AlbumMetadataInteractionsAddTo
from vimeo_python_sdk.type.album_metadata_interactions_add_videos import AlbumMetadataInteractionsAddVideos

class RequiredAlbumMetadataInteractions(TypedDict):
    add_custom_thumbnails: AlbumMetadataInteractionsAddCustomThumbnails

    add_live_events: AlbumMetadataInteractionsAddLiveEvents

    add_logos: AlbumMetadataInteractionsAddLogos

    add_to: AlbumMetadataInteractionsAddTo

    add_videos: AlbumMetadataInteractionsAddVideos

class OptionalAlbumMetadataInteractions(TypedDict, total=False):
    pass

class AlbumMetadataInteractions(RequiredAlbumMetadataInteractions, OptionalAlbumMetadataInteractions):
    pass

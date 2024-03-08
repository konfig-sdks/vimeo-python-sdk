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

from vimeo_python_sdk.type.album_metadata_interactions_add_custom_thumbnails_options import AlbumMetadataInteractionsAddCustomThumbnailsOptions

class RequiredAlbumMetadataInteractionsAddCustomThumbnails(TypedDict):
    options: AlbumMetadataInteractionsAddCustomThumbnailsOptions

    # The API URI that resolves to the connection data. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalAlbumMetadataInteractionsAddCustomThumbnails(TypedDict, total=False):
    pass

class AlbumMetadataInteractionsAddCustomThumbnails(RequiredAlbumMetadataInteractionsAddCustomThumbnails, OptionalAlbumMetadataInteractionsAddCustomThumbnails):
    pass

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

from vimeo_python_sdk.type.channel_metadata_interactions_moderate_videos_options import ChannelMetadataInteractionsModerateVideosOptions

class RequiredChannelMetadataInteractionsModerateVideos(TypedDict):
    options: ChannelMetadataInteractionsModerateVideosOptions

    # The API URI that resolves to the connection data. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalChannelMetadataInteractionsModerateVideos(TypedDict, total=False):
    pass

class ChannelMetadataInteractionsModerateVideos(RequiredChannelMetadataInteractionsModerateVideos, OptionalChannelMetadataInteractionsModerateVideos):
    pass

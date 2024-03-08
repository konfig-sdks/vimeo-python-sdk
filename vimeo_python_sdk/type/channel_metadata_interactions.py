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

from vimeo_python_sdk.type.channel_metadata_interactions_add_moderators import ChannelMetadataInteractionsAddModerators
from vimeo_python_sdk.type.channel_metadata_interactions_add_to import ChannelMetadataInteractionsAddTo
from vimeo_python_sdk.type.channel_metadata_interactions_follow import ChannelMetadataInteractionsFollow
from vimeo_python_sdk.type.channel_metadata_interactions_moderate_videos import ChannelMetadataInteractionsModerateVideos

class RequiredChannelMetadataInteractions(TypedDict):
    add_moderators: ChannelMetadataInteractionsAddModerators

    add_to: ChannelMetadataInteractionsAddTo

    follow: ChannelMetadataInteractionsFollow

    moderate_videos: ChannelMetadataInteractionsModerateVideos

class OptionalChannelMetadataInteractions(TypedDict, total=False):
    pass

class ChannelMetadataInteractions(RequiredChannelMetadataInteractions, OptionalChannelMetadataInteractions):
    pass

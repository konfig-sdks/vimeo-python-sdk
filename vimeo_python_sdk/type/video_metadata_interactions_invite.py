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

from vimeo_python_sdk.type.video_metadata_interactions_invite_options import VideoMetadataInteractionsInviteOptions

class RequiredVideoMetadataInteractionsInvite(TypedDict):
    options: VideoMetadataInteractionsInviteOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsInvite(TypedDict, total=False):
    pass

class VideoMetadataInteractionsInvite(RequiredVideoMetadataInteractionsInvite, OptionalVideoMetadataInteractionsInvite):
    pass

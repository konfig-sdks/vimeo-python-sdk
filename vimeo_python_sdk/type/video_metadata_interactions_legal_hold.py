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

from vimeo_python_sdk.type.video_metadata_interactions_legal_hold_options import VideoMetadataInteractionsLegalHoldOptions

class RequiredVideoMetadataInteractionsLegalHold(TypedDict):
    options: VideoMetadataInteractionsLegalHoldOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsLegalHold(TypedDict, total=False):
    pass

class VideoMetadataInteractionsLegalHold(RequiredVideoMetadataInteractionsLegalHold, OptionalVideoMetadataInteractionsLegalHold):
    pass

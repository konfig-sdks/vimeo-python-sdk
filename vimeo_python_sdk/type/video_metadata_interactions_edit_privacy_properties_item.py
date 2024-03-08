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

from vimeo_python_sdk.type.video_metadata_interactions_edit_privacy_properties_item_options import VideoMetadataInteractionsEditPrivacyPropertiesItemOptions

class RequiredVideoMetadataInteractionsEditPrivacyPropertiesItem(TypedDict):
    # The name of the property to be sent.
    name: str

    options: VideoMetadataInteractionsEditPrivacyPropertiesItemOptions

    # Whether the field must be sent to achieve the desired action.
    required: bool

class OptionalVideoMetadataInteractionsEditPrivacyPropertiesItem(TypedDict, total=False):
    pass

class VideoMetadataInteractionsEditPrivacyPropertiesItem(RequiredVideoMetadataInteractionsEditPrivacyPropertiesItem, OptionalVideoMetadataInteractionsEditPrivacyPropertiesItem):
    pass

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

from vimeo_python_sdk.type.video_metadata_interactions_edit_privacy_content_rating import VideoMetadataInteractionsEditPrivacyContentRating
from vimeo_python_sdk.type.video_metadata_interactions_edit_privacy_options import VideoMetadataInteractionsEditPrivacyOptions
from vimeo_python_sdk.type.video_metadata_interactions_edit_privacy_properties import VideoMetadataInteractionsEditPrivacyProperties

class RequiredVideoMetadataInteractionsEditPrivacy(TypedDict):
    content_rating: VideoMetadataInteractionsEditPrivacyContentRating

    options: VideoMetadataInteractionsEditPrivacyOptions

    properties: VideoMetadataInteractionsEditPrivacyProperties

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsEditPrivacy(TypedDict, total=False):
    pass

class VideoMetadataInteractionsEditPrivacy(RequiredVideoMetadataInteractionsEditPrivacy, OptionalVideoMetadataInteractionsEditPrivacy):
    pass

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

from vimeo_python_sdk.type.video_metadata_connections import VideoMetadataConnections
from vimeo_python_sdk.type.video_metadata_interactions import VideoMetadataInteractions

class RequiredVideoMetadata(TypedDict):
    connections: VideoMetadataConnections

    # Whether the video has chapter suggestions.
    has_chapter_suggestions: bool

    interactions: VideoMetadataInteractions

    # Whether the video is a screen recording.
    is_screen_record: bool

    # Whether the video is a Vimeo Create video.
    is_vimeo_create: bool

    # Whether the video is a webinar.
    is_webinar: bool

    # Whether the video is a Zoom upload.
    is_zoom_upload: bool

class OptionalVideoMetadata(TypedDict, total=False):
    # Whether the video can be replaced.
    can_be_replaced: bool

    # Whether the video has the email capture feature.
    has_email_capture: bool

class VideoMetadata(RequiredVideoMetadata, OptionalVideoMetadata):
    pass

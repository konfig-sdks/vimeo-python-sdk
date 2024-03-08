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
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.video_metadata_connections import VideoMetadataConnections
from vimeo_python_sdk.pydantic.video_metadata_interactions import VideoMetadataInteractions

class VideoMetadata(BaseModel):
    connections: VideoMetadataConnections = Field(alias='connections')

    # Whether the video has chapter suggestions.
    has_chapter_suggestions: bool = Field(alias='has_chapter_suggestions')

    interactions: VideoMetadataInteractions = Field(alias='interactions')

    # Whether the video is a screen recording.
    is_screen_record: bool = Field(alias='is_screen_record')

    # Whether the video is a Vimeo Create video.
    is_vimeo_create: bool = Field(alias='is_vimeo_create')

    # Whether the video is a webinar.
    is_webinar: bool = Field(alias='is_webinar')

    # Whether the video is a Zoom upload.
    is_zoom_upload: bool = Field(alias='is_zoom_upload')

    # Whether the video can be replaced.
    can_be_replaced: typing.Optional[bool] = Field(None, alias='can_be_replaced')

    # Whether the video has the email capture feature.
    has_email_capture: typing.Optional[bool] = Field(None, alias='has_email_capture')
    class Config:
        arbitrary_types_allowed = True

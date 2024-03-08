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

from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_embed_buttons import VideosUploadsBeginVideoUploadProcessRequestEmbedButtons
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_embed_end_screen import VideosUploadsBeginVideoUploadProcessRequestEmbedEndScreen
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_embed_logos import VideosUploadsBeginVideoUploadProcessRequestEmbedLogos
from vimeo_python_sdk.pydantic.videos_uploads_begin_video_upload_process_request_embed_title import VideosUploadsBeginVideoUploadProcessRequestEmbedTitle

class VideosUploadsBeginVideoUploadProcessRequestEmbed(BaseModel):
    title: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestEmbedTitle] = Field(None, alias='title')

    buttons: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestEmbedButtons] = Field(None, alias='buttons')

    # The main color of the embeddable player.
    color: typing.Optional[str] = Field(None, alias='color')

    end_screen: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestEmbedEndScreen] = Field(None, alias='end_screen')

    logos: typing.Optional[VideosUploadsBeginVideoUploadProcessRequestEmbedLogos] = Field(None, alias='logos')

    # Whether to show the playbar on the embeddable player.
    playbar: typing.Optional[bool] = Field(None, alias='playbar')

    # Whether to show the volume selector on the embeddable player.
    volume: typing.Optional[bool] = Field(None, alias='volume')
    class Config:
        arbitrary_types_allowed = True

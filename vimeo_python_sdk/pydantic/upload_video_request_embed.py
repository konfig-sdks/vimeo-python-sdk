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

from vimeo_python_sdk.pydantic.upload_video_request_embed_buttons import UploadVideoRequestEmbedButtons
from vimeo_python_sdk.pydantic.upload_video_request_embed_end_screen import UploadVideoRequestEmbedEndScreen
from vimeo_python_sdk.pydantic.upload_video_request_embed_logos import UploadVideoRequestEmbedLogos
from vimeo_python_sdk.pydantic.upload_video_request_embed_title import UploadVideoRequestEmbedTitle

class UploadVideoRequestEmbed(BaseModel):
    title: typing.Optional[UploadVideoRequestEmbedTitle] = Field(None, alias='title')

    buttons: typing.Optional[UploadVideoRequestEmbedButtons] = Field(None, alias='buttons')

    # The main color of the embeddable player.
    color: typing.Optional[str] = Field(None, alias='color')

    end_screen: typing.Optional[UploadVideoRequestEmbedEndScreen] = Field(None, alias='end_screen')

    logos: typing.Optional[UploadVideoRequestEmbedLogos] = Field(None, alias='logos')

    # Whether to show the playbar on the embeddable player.
    playbar: typing.Optional[bool] = Field(None, alias='playbar')

    # Whether to show the volume selector on the embeddable player.
    volume: typing.Optional[bool] = Field(None, alias='volume')
    class Config:
        arbitrary_types_allowed = True

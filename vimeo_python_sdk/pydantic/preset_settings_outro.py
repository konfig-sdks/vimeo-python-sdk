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

from vimeo_python_sdk.pydantic.preset_settings_outro_link import PresetSettingsOutroLink

class PresetSettingsOutro(BaseModel):
    # The preset outro type.  Option descriptions:  * `link` - The outro includes a link.  * `no idea` - The outro type is `no idea`. The outro includes uploaded videos.  * `text` - The outro includes text.  * `uploaded_clips` - The outro includes uploaded videos.  * `uploaded_videos` - The outro includes uploaded videos. 
    type: Literal["link", "no idea", "text", "uploaded_clips", "uploaded_videos"] = Field(alias='type')

    # A comma-separated list of video URIs. This field appears only when **type** is `uploaded_clips`.
    clips: typing.Optional[typing.Optional[str]] = Field(None, alias='clips')

    link: typing.Optional[PresetSettingsOutroLink] = Field(None, alias='link')

    # The outro text. This appears only when **type** is `text`.
    text: typing.Optional[typing.Optional[str]] = Field(None, alias='text')

    # A comma-separated list of video URIs. This field appears only when **type** is `no idea`.
    videos: typing.Optional[typing.Optional[str]] = Field(None, alias='videos')
    class Config:
        arbitrary_types_allowed = True

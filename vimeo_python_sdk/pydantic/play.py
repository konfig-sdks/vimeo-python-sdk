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

from vimeo_python_sdk.pydantic.hls_dash_video_file import HlsDashVideoFile
from vimeo_python_sdk.pydantic.play_progressive import PlayProgressive

class Play(BaseModel):
    # The play status of the video.  Option descriptions:  * `playable` - The video is playable.  * `purchase_required` - The video must be purchased.  * `restricted` - Playback for the video is restricted.  * `unavailable` - The video is unavailable. 
    status: Literal["playable", "purchase_required", "restricted", "unavailable"] = Field(alias='status')

    # The DASH video file.
    dash: typing.Optional[HlsDashVideoFile] = Field(None, alias='dash')

    # The HLS video file.
    hls: typing.Optional[HlsDashVideoFile] = Field(None, alias='hls')

    progressive: typing.Optional[PlayProgressive] = Field(None, alias='progressive')
    class Config:
        arbitrary_types_allowed = True

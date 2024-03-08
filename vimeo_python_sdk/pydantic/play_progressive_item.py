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


class PlayProgressiveItem(BaseModel):
    # The codec of the video file.  Option descriptions:  * `AV1` - The codec is AV1.  * `H264` - The codec is H264.  * `HEVC` - The codec is HEVC. 
    codec: Literal["AV1", "H264", "HEVC"] = Field(alias='codec')

    # The time in ISO 8601 format when the video file was created.
    created_time: str = Field(alias='created_time')

    # The frames per second of the video.
    fps: typing.Union[int, float] = Field(alias='fps')

    # The height of the video in pixels.
    height: typing.Optional[typing.Union[int, float]] = Field(alias='height')

    # The direct link to the video file.
    link: str = Field(alias='link')

    # The time in ISO 8601 format when the link to the video file expires.
    link_expiration_time: str = Field(alias='link_expiration_time')

    # The MD5 hash of the video file.
    md5: str = Field(alias='md5')

    # The video rendition.  Option descriptions:  * `1080p` - The video has 1080p resolution.  * `240p` - The video has 240p resolution.  * `2k` - The video has 2K resolution.  * `360p` - The video has 360p resolution.  * `480p` - The video has 480p resolution.  * `4k` - The video has 4K resolution.  * `540p` - The video has 540p resolution.  * `5k` - The video has 5K resolution.  * `6k` - The video has 6K resolution.  * `720p` - The video has 720p resolution.  * `7k` - The video has 7K resolution.  * `8k` - The video has 8K resolution. 
    rendition: Literal["1080p", "240p", "2k", "360p", "480p", "4k", "540p", "5k", "6k", "720p", "7k", "8k"] = Field(alias='rendition')

    # The size in bytes of the video file.
    size: typing.Optional[typing.Union[int, float]] = Field(alias='size')

    # The type of video file.  Option descriptions:  * `source` - The video file is a source file.  * `video/mp4` - The video file is in MP4 format.  * `video/webm` - The video file is in WebM format.  * `vp6/x-video` - The video file is in VP6 format. 
    type: Literal["source", "video/mp4", "video/webm", "vp6/x-video"] = Field(alias='type')

    # The width of the video in pixels.
    width: typing.Optional[typing.Union[int, float]] = Field(alias='width')

    # The URLs for logging events.
    log: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='log')
    class Config:
        arbitrary_types_allowed = True

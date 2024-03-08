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

from vimeo_python_sdk.type.hls_dash_video_file import HlsDashVideoFile
from vimeo_python_sdk.type.play_progressive import PlayProgressive

class RequiredPlay(TypedDict):
    # The play status of the video.  Option descriptions:  * `playable` - The video is playable.  * `purchase_required` - The video must be purchased.  * `restricted` - Playback for the video is restricted.  * `unavailable` - The video is unavailable. 
    status: str

class OptionalPlay(TypedDict, total=False):
    # The DASH video file.
    dash: HlsDashVideoFile

    # The HLS video file.
    hls: HlsDashVideoFile

    progressive: PlayProgressive

class Play(RequiredPlay, OptionalPlay):
    pass

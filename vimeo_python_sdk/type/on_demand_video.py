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

from vimeo_python_sdk.type.on_demand_video_buy import OnDemandVideoBuy
from vimeo_python_sdk.type.on_demand_video_interactions import OnDemandVideoInteractions
from vimeo_python_sdk.type.on_demand_video_metadata import OnDemandVideoMetadata
from vimeo_python_sdk.type.on_demand_video_options import OnDemandVideoOptions
from vimeo_python_sdk.type.on_demand_video_rent import OnDemandVideoRent
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.user import User

class RequiredOnDemandVideo(TypedDict):
    buy: OnDemandVideoBuy

    interactions: OnDemandVideoInteractions

    # The link to the video on Vimeo.
    link: str

    metadata: OnDemandVideoMetadata

    # The authenticated user's most recent play position in the video, in seconds.
    play_progress: typing.Union[int, float]

    # The year that the video was released.
    release_year: typing.Optional[typing.Union[int, float]]

    rent: OnDemandVideoRent

    # The type of video.  Option descriptions:  * `extra` - The video is an extra feature.  * `main` - The video is a main feature.  * `trailer` - The video is a trailer. 
    type: str

    # The video container's relative URI.
    uri: str

class OptionalOnDemandVideo(TypedDict, total=False):
    # The description of the video.
    description: str

    # The duration of the video.
    duration: str

    # The episode number of the video.
    episode: typing.Union[int, float]

    # The title of the video.
    name: str

    options: OnDemandVideoOptions

    # The active picture of the video.
    pictures: Picture

    # The position of the video relative to the other videos on the On Demand page.
    position: typing.Union[int, float]

    # The time in ISO 8601 format when the video was created or published.
    release_date: str

    # The owner of the video.
    user: User

class OnDemandVideo(RequiredOnDemandVideo, OptionalOnDemandVideo):
    pass

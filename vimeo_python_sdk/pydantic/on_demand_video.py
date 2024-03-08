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

from vimeo_python_sdk.pydantic.on_demand_video_buy import OnDemandVideoBuy
from vimeo_python_sdk.pydantic.on_demand_video_interactions import OnDemandVideoInteractions
from vimeo_python_sdk.pydantic.on_demand_video_metadata import OnDemandVideoMetadata
from vimeo_python_sdk.pydantic.on_demand_video_options import OnDemandVideoOptions
from vimeo_python_sdk.pydantic.on_demand_video_rent import OnDemandVideoRent
from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.user import User

class OnDemandVideo(BaseModel):
    buy: OnDemandVideoBuy = Field(alias='buy')

    interactions: OnDemandVideoInteractions = Field(alias='interactions')

    # The link to the video on Vimeo.
    link: str = Field(alias='link')

    metadata: OnDemandVideoMetadata = Field(alias='metadata')

    # The authenticated user's most recent play position in the video, in seconds.
    play_progress: typing.Union[int, float] = Field(alias='play_progress')

    # The year that the video was released.
    release_year: typing.Optional[typing.Union[int, float]] = Field(alias='release_year')

    rent: OnDemandVideoRent = Field(alias='rent')

    # The type of video.  Option descriptions:  * `extra` - The video is an extra feature.  * `main` - The video is a main feature.  * `trailer` - The video is a trailer. 
    type: Literal["extra", "main", "trailer"] = Field(alias='type')

    # The video container's relative URI.
    uri: str = Field(alias='uri')

    # The description of the video.
    description: typing.Optional[str] = Field(None, alias='description')

    # The duration of the video.
    duration: typing.Optional[str] = Field(None, alias='duration')

    # The episode number of the video.
    episode: typing.Optional[typing.Union[int, float]] = Field(None, alias='episode')

    # The title of the video.
    name: typing.Optional[str] = Field(None, alias='name')

    options: typing.Optional[OnDemandVideoOptions] = Field(None, alias='options')

    # The active picture of the video.
    pictures: typing.Optional[Picture] = Field(None, alias='pictures')

    # The position of the video relative to the other videos on the On Demand page.
    position: typing.Optional[typing.Union[int, float]] = Field(None, alias='position')

    # The time in ISO 8601 format when the video was created or published.
    release_date: typing.Optional[str] = Field(None, alias='release_date')

    # The owner of the video.
    user: typing.Optional[User] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True

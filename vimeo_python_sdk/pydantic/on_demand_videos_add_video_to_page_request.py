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

from vimeo_python_sdk.pydantic.on_demand_videos_add_video_to_page_request_buy import OnDemandVideosAddVideoToPageRequestBuy
from vimeo_python_sdk.pydantic.on_demand_videos_add_video_to_page_request_rent import OnDemandVideosAddVideoToPageRequestRent

class OnDemandVideosAddVideoToPageRequest(BaseModel):
    # The type of the video.  Option descriptions:  * `extra` - The video type is extra footage.  * `main` - The video type is the main video.  * `trailer` - The video type is a trailer. 
    type: Literal["extra", "main", "trailer"] = Field(alias='type')

    buy: typing.Optional[OnDemandVideosAddVideoToPageRequestBuy] = Field(None, alias='buy')

    # The position of the video in the On Demand collection.
    position: typing.Optional[typing.Union[int, float]] = Field(None, alias='position')

    # The release year of the video.
    release_year: typing.Optional[typing.Union[int, float]] = Field(None, alias='release_year')

    rent: typing.Optional[OnDemandVideosAddVideoToPageRequestRent] = Field(None, alias='rent')
    class Config:
        arbitrary_types_allowed = True

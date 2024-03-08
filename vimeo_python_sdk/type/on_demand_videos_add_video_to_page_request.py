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

from vimeo_python_sdk.type.on_demand_videos_add_video_to_page_request_buy import OnDemandVideosAddVideoToPageRequestBuy
from vimeo_python_sdk.type.on_demand_videos_add_video_to_page_request_rent import OnDemandVideosAddVideoToPageRequestRent

class RequiredOnDemandVideosAddVideoToPageRequest(TypedDict):
    # The type of the video.  Option descriptions:  * `extra` - The video type is extra footage.  * `main` - The video type is the main video.  * `trailer` - The video type is a trailer. 
    type: str

class OptionalOnDemandVideosAddVideoToPageRequest(TypedDict, total=False):
    buy: OnDemandVideosAddVideoToPageRequestBuy

    # The position of the video in the On Demand collection.
    position: typing.Union[int, float]

    # The release year of the video.
    release_year: typing.Union[int, float]

    rent: OnDemandVideosAddVideoToPageRequestRent

class OnDemandVideosAddVideoToPageRequest(RequiredOnDemandVideosAddVideoToPageRequest, OptionalOnDemandVideosAddVideoToPageRequest):
    pass

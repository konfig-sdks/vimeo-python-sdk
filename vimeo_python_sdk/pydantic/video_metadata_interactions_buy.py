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


class VideoMetadataInteractionsBuy(BaseModel):
    # The currency code for the user's region.
    currency: typing.Optional[str] = Field(alias='currency')

    # The formatted display price for buying the On Demand video.
    display_price: typing.Optional[str] = Field(alias='display_price')

    # The user's download access to the On Demand video.  Option descriptions:  * `available` - The video is available for download.  * `purchased` - The user has purchased the video.  * `restricted` - The user isn't permitted to download the video.  * `unavailable` - The video isn't available for download. 
    download: Literal["available", "purchased", "restricted", "unavailable"] = Field(alias='download')

    # Whether the On Demand video has DRM.
    drm: bool = Field(alias='drm')

    # The URL to buy the On Demand video on Vimeo.
    link: typing.Optional[str] = Field(alias='link')

    # The price to buy the On Demand video.
    price: typing.Optional[typing.Union[int, float]] = Field(alias='price')

    # The time in ISO 8601 format when the On Demand video was purchased.
    purchase_time: typing.Optional[str] = Field(alias='purchase_time')

    # The user's streaming access to the On Demand video.  Option descriptions:  * `available` - The video is available for streaming.  * `purchased` - The user has purchased the video.  * `restricted` - The user isn't permitted to stream the video.  * `unavailable` - The video isn't available for streaming 
    stream: Literal["available", "purchased", "restricted", "unavailable"] = Field(alias='stream')

    # The product URI to purchase the On Demand video.
    uri: typing.Optional[str] = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

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


class RequiredVideoMetadataInteractionsRent(TypedDict):
    # The currency code for the user's region.
    currency: typing.Optional[str]

    # The formatted display price for renting the On Demand video.
    display_price: typing.Optional[str]

    # Whether the On Demand video has DRM.
    drm: bool

    # The time in ISO 8601 format when the rental period for the On Demand video expires.
    expires_time: typing.Optional[str]

    # The URL to rent the On Demand video on Vimeo.
    link: typing.Optional[str]

    # The price to buy the On Demand video.
    price: typing.Optional[typing.Union[int, float]]

    # The time in ISO 8601 format when the On Demand video was rented.
    purchase_time: typing.Optional[str]

    # The user's streaming access to the On Demand video.  Option descriptions:  * `available` - The video is available for streaming.  * `purchased` - The user has purchased the video.  * `restricted` - The user isn't permitted to stream the video.  * `unavailable` - The video isn't available for streaming. 
    stream: str

    # The product URI to rent the On Demand video.
    uri: typing.Optional[str]

class OptionalVideoMetadataInteractionsRent(TypedDict, total=False):
    pass

class VideoMetadataInteractionsRent(RequiredVideoMetadataInteractionsRent, OptionalVideoMetadataInteractionsRent):
    pass

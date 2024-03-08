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


class RequiredCreateVodRequestEpisodesRentPrice(TypedDict):
    pass

class OptionalCreateVodRequestEpisodesRentPrice(TypedDict, total=False):
    # The rental price per episode in United States dollars. This parameter is applicable only when **type** is `series`, and it's required when **episode.rent.active** is `true`.
    USD: typing.Union[int, float]

class CreateVodRequestEpisodesRentPrice(RequiredCreateVodRequestEpisodesRentPrice, OptionalCreateVodRequestEpisodesRentPrice):
    pass

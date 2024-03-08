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


class RequiredOnDemandPageEpisodesBuy(TypedDict):
    # Whether all the videos on the On Demand page can be purchased as a whole.
    active: bool

    # The default price to buy an episode.
    price: typing.Optional[typing.Union[int, float]]

class OptionalOnDemandPageEpisodesBuy(TypedDict, total=False):
    pass

class OnDemandPageEpisodesBuy(RequiredOnDemandPageEpisodesBuy, OptionalOnDemandPageEpisodesBuy):
    pass

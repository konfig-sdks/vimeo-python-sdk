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


class RequiredOnDemandEssentialsCreatePageRequestEpisodesBuyPrice(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestEpisodesBuyPrice(TypedDict, total=False):
    # The purchase price per episode in United States dollars. This parameter is required when **episodes.buy.active** is `true`.
    USD: typing.Union[int, float]

class OnDemandEssentialsCreatePageRequestEpisodesBuyPrice(RequiredOnDemandEssentialsCreatePageRequestEpisodesBuyPrice, OptionalOnDemandEssentialsCreatePageRequestEpisodesBuyPrice):
    pass

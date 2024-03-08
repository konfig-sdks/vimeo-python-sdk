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

from vimeo_python_sdk.type.on_demand_page_episodes_buy import OnDemandPageEpisodesBuy
from vimeo_python_sdk.type.on_demand_page_episodes_rent import OnDemandPageEpisodesRent

class RequiredOnDemandPageEpisodes(TypedDict):
    buy: OnDemandPageEpisodesBuy

    rent: OnDemandPageEpisodesRent

class OptionalOnDemandPageEpisodes(TypedDict, total=False):
    pass

class OnDemandPageEpisodes(RequiredOnDemandPageEpisodes, OptionalOnDemandPageEpisodes):
    pass

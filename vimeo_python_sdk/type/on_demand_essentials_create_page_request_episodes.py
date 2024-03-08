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

from vimeo_python_sdk.type.on_demand_essentials_create_page_request_episodes_buy import OnDemandEssentialsCreatePageRequestEpisodesBuy
from vimeo_python_sdk.type.on_demand_essentials_create_page_request_episodes_rent import OnDemandEssentialsCreatePageRequestEpisodesRent

class RequiredOnDemandEssentialsCreatePageRequestEpisodes(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestEpisodes(TypedDict, total=False):
    buy: OnDemandEssentialsCreatePageRequestEpisodesBuy

    rent: OnDemandEssentialsCreatePageRequestEpisodesRent

class OnDemandEssentialsCreatePageRequestEpisodes(RequiredOnDemandEssentialsCreatePageRequestEpisodes, OptionalOnDemandEssentialsCreatePageRequestEpisodes):
    pass

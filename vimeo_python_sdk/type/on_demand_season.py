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

from vimeo_python_sdk.type.on_demand_season_metadata import OnDemandSeasonMetadata
from vimeo_python_sdk.type.user import User

class RequiredOnDemandSeason(TypedDict):
    # The description of the season.
    description: str

    metadata: OnDemandSeasonMetadata

    # The name of the season.
    name: str

    # The position of the season relative to other seasons in the series.
    position: typing.Union[int, float]

    # The unique identifier of the On Demand season.
    resource_key: str

    # The type of the season.
    type: str

    # The season container's relative URI.
    uri: str

    # The creator of the season's On Demand page.
    user: User

class OptionalOnDemandSeason(TypedDict, total=False):
    pass

class OnDemandSeason(RequiredOnDemandSeason, OptionalOnDemandSeason):
    pass

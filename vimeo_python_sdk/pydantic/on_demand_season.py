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

from vimeo_python_sdk.pydantic.on_demand_season_metadata import OnDemandSeasonMetadata
from vimeo_python_sdk.pydantic.user import User

class OnDemandSeason(BaseModel):
    # The description of the season.
    description: str = Field(alias='description')

    metadata: OnDemandSeasonMetadata = Field(alias='metadata')

    # The name of the season.
    name: str = Field(alias='name')

    # The position of the season relative to other seasons in the series.
    position: typing.Union[int, float] = Field(alias='position')

    # The unique identifier of the On Demand season.
    resource_key: str = Field(alias='resource_key')

    # The type of the season.
    type: str = Field(alias='type')

    # The season container's relative URI.
    uri: str = Field(alias='uri')

    # The creator of the season's On Demand page.
    user: User = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True

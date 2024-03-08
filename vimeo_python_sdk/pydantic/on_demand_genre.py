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

from vimeo_python_sdk.pydantic.on_demand_genre_interactions import OnDemandGenreInteractions
from vimeo_python_sdk.pydantic.on_demand_genre_metadata import OnDemandGenreMetadata

class OnDemandGenre(BaseModel):
    # The canonical name or URL slug of the genre.
    canonical: str = Field(alias='canonical')

    interactions: OnDemandGenreInteractions = Field(alias='interactions')

    # The Vimeo URL for the genre.
    link: str = Field(alias='link')

    metadata: OnDemandGenreMetadata = Field(alias='metadata')

    # The descriptive name of the genre.
    name: str = Field(alias='name')

    # The relative URI of the On Demand genre.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.type.on_demand_genre_interactions import OnDemandGenreInteractions
from vimeo_python_sdk.type.on_demand_genre_metadata import OnDemandGenreMetadata

class RequiredOnDemandGenre(TypedDict):
    # The canonical name or URL slug of the genre.
    canonical: str

    interactions: OnDemandGenreInteractions

    # The Vimeo URL for the genre.
    link: str

    metadata: OnDemandGenreMetadata

    # The descriptive name of the genre.
    name: str

    # The relative URI of the On Demand genre.
    uri: str

class OptionalOnDemandGenre(TypedDict, total=False):
    pass

class OnDemandGenre(RequiredOnDemandGenre, OptionalOnDemandGenre):
    pass

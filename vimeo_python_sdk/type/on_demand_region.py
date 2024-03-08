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


class RequiredOnDemandRegion(TypedDict):
    # The ISO 3166-1 alpha-2 code for this country.
    country_code: str

    # The descriptive name of this country.
    country_name: str

    # The region container's relative URI.
    uri: str

class OptionalOnDemandRegion(TypedDict, total=False):
    pass

class OnDemandRegion(RequiredOnDemandRegion, OptionalOnDemandRegion):
    pass

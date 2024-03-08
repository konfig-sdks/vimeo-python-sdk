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

from vimeo_python_sdk.type.on_demand_video_interactions_page import OnDemandVideoInteractionsPage

class RequiredOnDemandVideoInteractions(TypedDict):
    page: OnDemandVideoInteractionsPage

class OptionalOnDemandVideoInteractions(TypedDict, total=False):
    pass

class OnDemandVideoInteractions(RequiredOnDemandVideoInteractions, OptionalOnDemandVideoInteractions):
    pass

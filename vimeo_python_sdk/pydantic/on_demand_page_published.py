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


class OnDemandPagePublished(BaseModel):
    # Whether the On Demand page has been published.
    enabled: bool = Field(alias='enabled')

    # The time in ISO 8601 format when this page was published.
    time: str = Field(alias='time')
    class Config:
        arbitrary_types_allowed = True

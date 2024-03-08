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


class OnDemandPagePreorder(BaseModel):
    # Whether the On Demand page is available for preorder.
    active: bool = Field(alias='active')

    # The time in ISO 8601 format when the preorder was cancelled.
    cancel_time: str = Field(alias='cancel_time')

    # The time in ISO 8601 format when the preorder was released to the public.
    publish_time: str = Field(alias='publish_time')

    # The time in ISO 8601 format when the preorder started.
    time: str = Field(alias='time')
    class Config:
        arbitrary_types_allowed = True

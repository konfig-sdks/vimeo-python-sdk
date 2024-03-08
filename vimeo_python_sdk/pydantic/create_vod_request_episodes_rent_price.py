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


class CreateVodRequestEpisodesRentPrice(BaseModel):
    # The rental price per episode in United States dollars. This parameter is applicable only when **type** is `series`, and it's required when **episode.rent.active** is `true`.
    u_s_d: typing.Optional[typing.Union[int, float]] = Field(None, alias='USD')
    class Config:
        arbitrary_types_allowed = True

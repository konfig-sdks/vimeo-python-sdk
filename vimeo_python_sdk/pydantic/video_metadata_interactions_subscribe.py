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


class VideoMetadataInteractionsSubscribe(BaseModel):
    # Whether the On Demand video has DRM.
    drm: typing.Optional[bool] = Field(None, alias='drm')

    # The time in ISO 8601 format when the subscription expires.
    expires_time: typing.Optional[str] = Field(None, alias='expires_time')

    # The time in ISO 8601 format when the subscription was purchased.
    purchase_time: typing.Optional[str] = Field(None, alias='purchase_time')

    # The stream type.
    stream: typing.Optional[str] = Field(None, alias='stream')
    class Config:
        arbitrary_types_allowed = True

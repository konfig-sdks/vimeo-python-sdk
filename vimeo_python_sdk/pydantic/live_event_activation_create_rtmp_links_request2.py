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


class LiveEventActivationCreateRtmpLinksRequest2(BaseModel):
    # Whether the stream activates from the cloud composer. _This field is deprecated._
    cloud_composing_streaming: typing.Optional[bool] = Field(None, alias='cloud_composing_streaming')

    # Whether the stream activates from the cloud composer.
    streaming_start_requested: typing.Optional[bool] = Field(None, alias='streaming_start_requested')
    class Config:
        arbitrary_types_allowed = True

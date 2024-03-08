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

from vimeo_python_sdk.pydantic.create_vod_request_episodes_buy_price import CreateVodRequestEpisodesBuyPrice

class CreateVodRequestEpisodesBuy(BaseModel):
    # Whether episodes can be purchased.
    active: typing.Optional[bool] = Field(None, alias='active')

    # Whether people who buy episodes can download them. To use this parameter, **type** must be `series`.
    download: typing.Optional[bool] = Field(None, alias='download')

    price: typing.Optional[CreateVodRequestEpisodesBuyPrice] = Field(None, alias='price')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.create_vod_request_rent_price import CreateVodRequestRentPrice

class CreateVodRequestRent(BaseModel):
    # Whether the video can be rented. This parameter is required when **episodes.rent.active** is `true`.
    active: typing.Optional[bool] = Field(None, alias='active')

    # The rental period of the video.  Option descriptions:  * `1 week` - The video can be rented for a maximum of 1 week.  * `1 year` - The video can be rented for a maximum of 1 year.  * `24 hour` - The video can be rented for a maximum of 24 hours.  * `3 month` - The video can be rented for a maximum of 3 months.  * `30 day` - The video can be rented for a maximum of 30 days.  * `48 hour` - The video can be rented for a maximum of 48 hours.  * `6 month` - The video can be rented for a maximum of 6 months.  * `72 hour` - The video can be rented for a maximum of 72 hours. 
    period: typing.Optional[Literal["1 week", "1 year", "24 hour", "3 month", "30 day", "48 hour", "6 month", "72 hour"]] = Field(None, alias='period')

    price: typing.Optional[CreateVodRequestRentPrice] = Field(None, alias='price')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.create_vod_request_episodes_rent_price import CreateVodRequestEpisodesRentPrice

class CreateVodRequestEpisodesRent(BaseModel):
    # Whether episodes can be rented.
    active: typing.Optional[bool] = Field(None, alias='active')

    # The rental period of the episode.  Option descriptions:  * `1 week` - The episode can be rented for a maximum of 1 week.  * `1 year` - The episode can be rented for a maximum of 1 year.  * `24 hour` - The episode can be rented for a maximum of 24 hours.  * `3 month` - The episode can be rented for a maximum of 3 months.  * `30 day` - The episode can be rented for a maximum of 30 days.  * `48 hour` - The episode can be rented for a maximum of 48 hours.  * `6 month` - The episode can be rented for a maximum of 6 months.  * `72 hour` - The episode can be rented for a maximum of 72 hours. 
    period: typing.Optional[Literal["1 week", "1 year", "24 hour", "3 month", "30 day", "48 hour", "6 month", "72 hour"]] = Field(None, alias='period')

    price: typing.Optional[CreateVodRequestEpisodesRentPrice] = Field(None, alias='price')
    class Config:
        arbitrary_types_allowed = True

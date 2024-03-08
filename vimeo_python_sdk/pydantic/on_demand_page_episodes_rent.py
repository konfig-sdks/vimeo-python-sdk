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


class OnDemandPageEpisodesRent(BaseModel):
    # Whether all the videos on the On Demand page can be rented as a whole.
    active: bool = Field(alias='active')

    # The rental period for the video.  Option descriptions:  * `1 day` - The rental period is one day.  * `1 month` - The rental period is one month.  * `1 week` - The rental period is one week.  * `1 year` - The rental period is one year.  * `2 day` - The rental period is two days.  * `24 hour` - The rental period is 24 hours.  * `3 day` - The rental period is three days.  * `3 month` - The rental period is three months.  * `30 day` - The rental period is 30 days.  * `48 hour` - The rental period is 48 hours.  * `6 month` - The rental period is six months.  * `60 day` - The rental period is 60 days.  * `7 day` - The rental period is 7 days.  * `72 hour` - The rental period is 72 hours. 
    period: Literal["1 day", "1 month", "1 week", "1 year", "2 day", "24 hour", "3 day", "3 month", "30 day", "48 hour", "6 month", "60 day", "7 day", "72 hour"] = Field(alias='period')

    # The default price to rent an episode.
    price: typing.Optional[typing.Union[int, float]] = Field(alias='price')
    class Config:
        arbitrary_types_allowed = True

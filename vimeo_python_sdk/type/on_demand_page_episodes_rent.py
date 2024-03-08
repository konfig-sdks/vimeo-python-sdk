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


class RequiredOnDemandPageEpisodesRent(TypedDict):
    # Whether all the videos on the On Demand page can be rented as a whole.
    active: bool

    # The rental period for the video.  Option descriptions:  * `1 day` - The rental period is one day.  * `1 month` - The rental period is one month.  * `1 week` - The rental period is one week.  * `1 year` - The rental period is one year.  * `2 day` - The rental period is two days.  * `24 hour` - The rental period is 24 hours.  * `3 day` - The rental period is three days.  * `3 month` - The rental period is three months.  * `30 day` - The rental period is 30 days.  * `48 hour` - The rental period is 48 hours.  * `6 month` - The rental period is six months.  * `60 day` - The rental period is 60 days.  * `7 day` - The rental period is 7 days.  * `72 hour` - The rental period is 72 hours. 
    period: typing.Optional[str]

    # The default price to rent an episode.
    price: typing.Optional[typing.Union[int, float]]

class OptionalOnDemandPageEpisodesRent(TypedDict, total=False):
    pass

class OnDemandPageEpisodesRent(RequiredOnDemandPageEpisodesRent, OptionalOnDemandPageEpisodesRent):
    pass

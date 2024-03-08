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

from vimeo_python_sdk.type.on_demand_essentials_create_page_request_episodes_rent_price import OnDemandEssentialsCreatePageRequestEpisodesRentPrice

class RequiredOnDemandEssentialsCreatePageRequestEpisodesRent(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestEpisodesRent(TypedDict, total=False):
    # Whether episodes can be rented.
    active: bool

    # The rental period of the episode.  Option descriptions:  * `1 week` - The episode can be rented for a maximum of 1 week.  * `1 year` - The episode can be rented for a maximum of 1 year.  * `24 hour` - The episode can be rented for a maximum of 24 hours.  * `3 month` - The episode can be rented for a maximum of 3 months.  * `30 day` - The episode can be rented for a maximum of 30 days.  * `48 hour` - The episode can be rented for a maximum of 48 hours.  * `6 month` - The episode can be rented for a maximum of 6 months.  * `72 hour` - The episode can be rented for a maximum of 72 hours. 
    period: str

    price: OnDemandEssentialsCreatePageRequestEpisodesRentPrice

class OnDemandEssentialsCreatePageRequestEpisodesRent(RequiredOnDemandEssentialsCreatePageRequestEpisodesRent, OptionalOnDemandEssentialsCreatePageRequestEpisodesRent):
    pass

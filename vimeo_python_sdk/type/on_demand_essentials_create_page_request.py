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

from vimeo_python_sdk.type.on_demand_essentials_create_page_request_buy import OnDemandEssentialsCreatePageRequestBuy
from vimeo_python_sdk.type.on_demand_essentials_create_page_request_episodes import OnDemandEssentialsCreatePageRequestEpisodes
from vimeo_python_sdk.type.on_demand_essentials_create_page_request_rent import OnDemandEssentialsCreatePageRequestRent
from vimeo_python_sdk.type.on_demand_essentials_create_page_request_subscription import OnDemandEssentialsCreatePageRequestSubscription

class RequiredOnDemandEssentialsCreatePageRequest(TypedDict):
    # The description of the On Demand page.
    description: str

    # The content rating of the video, given either as a comma-separated list or as a JSON array, depending on the request format.  Option descriptions:  * `drugs` - The video contains drug or alcohol use.  * `language` - The video contains profanity or sexually suggestive content.  * `nudity` - The video contains nudity.  * `safe` - The video is suitable for all audiences.  * `unrated` - The video hasn't been rated.  * `violence` - The video contains violent or graphic content. 
    content_rating: str

    # The name of the On Demand page.
    name: str

    # The type of the On Demand page.  Option descriptions:  * `film` - The On Demand page is a film.  * `series` - The On Demand page is a series. 
    type: str

class OptionalOnDemandEssentialsCreatePageRequest(TypedDict, total=False):
    # An array of accepted currencies.  Option descriptions:  * `AUD` - The currency is in Australian dollars.  * `CAD` - The currency is in Canadian dollars.  * `CHF` - The currency is in Swiss francs.  * `DKK` - The currency is in Danish krone.  * `EUR` - The currency is in euros.  * `GBP` - The currency is in British pounds.  * `JPY` - The currency is in Japanese yen.  * `KRW` - The currency is in South Korean won.  * `NOK` - The currency is in Norwegian krone.  * `PLN` - The currency is in Polish zloty.  * `SEK` - The currency is in Swedish krona.  * `USD` - The currency is in United States dollars. 
    accepted_currencies: str

    buy: OnDemandEssentialsCreatePageRequestBuy

    # The custom domain of the On Demand page.
    domain_link: str

    episodes: OnDemandEssentialsCreatePageRequestEpisodes

    # The custom string to use in the Vimeo URL of the On Demand page.
    link: str

    rent: OnDemandEssentialsCreatePageRequestRent

    subscription: OnDemandEssentialsCreatePageRequestSubscription

class OnDemandEssentialsCreatePageRequest(RequiredOnDemandEssentialsCreatePageRequest, OptionalOnDemandEssentialsCreatePageRequest):
    pass

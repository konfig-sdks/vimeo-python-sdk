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

from vimeo_python_sdk.pydantic.create_vod_request_buy import CreateVodRequestBuy
from vimeo_python_sdk.pydantic.create_vod_request_episodes import CreateVodRequestEpisodes
from vimeo_python_sdk.pydantic.create_vod_request_rent import CreateVodRequestRent
from vimeo_python_sdk.pydantic.create_vod_request_subscription import CreateVodRequestSubscription

class CreateVodRequest(BaseModel):
    # The description of the On Demand page.
    description: str = Field(alias='description')

    # The content rating of the video, given either as a comma-separated list or as a JSON array, depending on the request format.  Option descriptions:  * `drugs` - The video contains drug or alcohol use.  * `language` - The video contains profanity or sexually suggestive content.  * `nudity` - The video contains nudity.  * `safe` - The video is suitable for all audiences.  * `unrated` - The video hasn't been rated.  * `violence` - The video contains violent or graphic content. 
    content_rating: Literal["drugs", "language", "nudity", "safe", "unrated", "violence"] = Field(alias='content_rating')

    # The name of the On Demand page.
    name: str = Field(alias='name')

    # The type of the On Demand page.  Option descriptions:  * `film` - The On Demand page is a film.  * `series` - The On Demand page is a series. 
    type: Literal["film", "series"] = Field(alias='type')

    # An array of accepted currencies.  Option descriptions:  * `AUD` - The currency is in Australian dollars.  * `CAD` - The currency is in Canadian dollars.  * `CHF` - The currency is in Swiss francs.  * `DKK` - The currency is in Danish krone.  * `EUR` - The currency is in euros.  * `GBP` - The currency is in British pounds.  * `JPY` - The currency is in Japanese yen.  * `KRW` - The currency is in South Korean won.  * `NOK` - The currency is in Norwegian krone.  * `PLN` - The currency is in Polish zloty.  * `SEK` - The currency is in Swedish krona.  * `USD` - The currency is in United States dollars. 
    accepted_currencies: typing.Optional[Literal["AUD", "CAD", "CHF", "DKK", "EUR", "GBP", "JPY", "KRW", "NOK", "PLN", "SEK", "USD"]] = Field(None, alias='accepted_currencies')

    buy: typing.Optional[CreateVodRequestBuy] = Field(None, alias='buy')

    # The custom domain of the On Demand page.
    domain_link: typing.Optional[str] = Field(None, alias='domain_link')

    episodes: typing.Optional[CreateVodRequestEpisodes] = Field(None, alias='episodes')

    # The custom string to use in the Vimeo URL of the On Demand page.
    link: typing.Optional[str] = Field(None, alias='link')

    rent: typing.Optional[CreateVodRequestRent] = Field(None, alias='rent')

    subscription: typing.Optional[CreateVodRequestSubscription] = Field(None, alias='subscription')
    class Config:
        arbitrary_types_allowed = True

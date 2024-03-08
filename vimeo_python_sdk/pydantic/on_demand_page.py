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

from vimeo_python_sdk.pydantic.on_demand_genre import OnDemandGenre
from vimeo_python_sdk.pydantic.on_demand_page_colors import OnDemandPageColors
from vimeo_python_sdk.pydantic.on_demand_page_content_rating import OnDemandPageContentRating
from vimeo_python_sdk.pydantic.on_demand_page_episodes import OnDemandPageEpisodes
from vimeo_python_sdk.pydantic.on_demand_page_metadata import OnDemandPageMetadata
from vimeo_python_sdk.pydantic.on_demand_page_preorder import OnDemandPagePreorder
from vimeo_python_sdk.pydantic.on_demand_page_published import OnDemandPagePublished
from vimeo_python_sdk.pydantic.on_demand_page_subscription import OnDemandPageSubscription
from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.video import Video

class OnDemandPage(BaseModel):
    # The description of the On Demand page.
    description: typing.Optional[str] = Field(alias='description')

    # The background image for the On Demand page.
    background: Picture = Field(alias='background')

    colors: OnDemandPageColors = Field(alias='colors')

    content_rating: OnDemandPageContentRating = Field(alias='content_rating')

    # The link to the On Demand page on its own domain.
    domain_link: typing.Optional[str] = Field(alias='domain_link')

    episodes: OnDemandPageEpisodes = Field(alias='episodes')

    # An array of the genres assigned to the On Demand page.
    genres: typing.List[OnDemandGenre] = Field(alias='genres')

    # The link to the On Demand page.
    link: str = Field(alias='link')

    metadata: OnDemandPageMetadata = Field(alias='metadata')

    # The descriptive title of the On Demand page.
    name: str = Field(alias='name')

    # The active poster for the On Demand page.
    pictures: Picture = Field(alias='pictures')

    preorder: OnDemandPagePreorder = Field(alias='preorder')

    published: OnDemandPagePublished = Field(alias='published')

    # The rating of the On Demand page.
    rating: typing.Optional[typing.Union[int, float]] = Field(alias='rating')

    # The On Demand resource key.
    resource_key: str = Field(alias='resource_key')

    subscription: OnDemandPageSubscription = Field(alias='subscription')

    # The graphical theme for the On Demand page.
    theme: str = Field(alias='theme')

    # The thumbnail image for the On Demand page.
    thumbnail: Picture = Field(alias='thumbnail')

    # The trailer for the On Demand page.
    trailer: Video = Field(alias='trailer')

    # Whether the On Demand page is for a film or a series.  Option descriptions:  * `film` - The On Demand page is for a film.  * `series` - The On Demand page is for a series. 
    type: Literal["film", "series"] = Field(alias='type')

    # The relative URI of the On Demand page.
    uri: str = Field(alias='uri')

    # The user who created the On Demand page.
    user: User = Field(alias='user')

    # The time in ISO 8601 format when the On Demand page was created.
    created_time: typing.Optional[str] = Field(None, alias='created_time')

    # The On Demand page's film, if the page is for a film.
    film: typing.Optional[Video] = Field(None, alias='film')

    # The time in ISO 8601 format when the On Demand page was last modified.
    modified_time: typing.Optional[str] = Field(None, alias='modified_time')

    # The creator-designated SKU for the On Demand page.
    sku: typing.Optional[typing.Optional[str]] = Field(None, alias='sku')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.type.on_demand_genre import OnDemandGenre
from vimeo_python_sdk.type.on_demand_page_colors import OnDemandPageColors
from vimeo_python_sdk.type.on_demand_page_content_rating import OnDemandPageContentRating
from vimeo_python_sdk.type.on_demand_page_episodes import OnDemandPageEpisodes
from vimeo_python_sdk.type.on_demand_page_metadata import OnDemandPageMetadata
from vimeo_python_sdk.type.on_demand_page_preorder import OnDemandPagePreorder
from vimeo_python_sdk.type.on_demand_page_published import OnDemandPagePublished
from vimeo_python_sdk.type.on_demand_page_subscription import OnDemandPageSubscription
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.video import Video

class RequiredOnDemandPage(TypedDict):
    # The description of the On Demand page.
    description: typing.Optional[str]

    # The background image for the On Demand page.
    background: Picture

    colors: OnDemandPageColors

    content_rating: OnDemandPageContentRating

    # The link to the On Demand page on its own domain.
    domain_link: typing.Optional[str]

    episodes: OnDemandPageEpisodes

    # An array of the genres assigned to the On Demand page.
    genres: typing.List[OnDemandGenre]

    # The link to the On Demand page.
    link: str

    metadata: OnDemandPageMetadata

    # The descriptive title of the On Demand page.
    name: str

    # The active poster for the On Demand page.
    pictures: Picture

    preorder: OnDemandPagePreorder

    published: OnDemandPagePublished

    # The rating of the On Demand page.
    rating: typing.Optional[typing.Union[int, float]]

    # The On Demand resource key.
    resource_key: str

    subscription: OnDemandPageSubscription

    # The graphical theme for the On Demand page.
    theme: str

    # The thumbnail image for the On Demand page.
    thumbnail: Picture

    # The trailer for the On Demand page.
    trailer: Video

    # Whether the On Demand page is for a film or a series.  Option descriptions:  * `film` - The On Demand page is for a film.  * `series` - The On Demand page is for a series. 
    type: str

    # The relative URI of the On Demand page.
    uri: str

    # The user who created the On Demand page.
    user: User

class OptionalOnDemandPage(TypedDict, total=False):
    # The time in ISO 8601 format when the On Demand page was created.
    created_time: str

    # The On Demand page's film, if the page is for a film.
    film: Video

    # The time in ISO 8601 format when the On Demand page was last modified.
    modified_time: str

    # The creator-designated SKU for the On Demand page.
    sku: typing.Optional[str]

class OnDemandPage(RequiredOnDemandPage, OptionalOnDemandPage):
    pass

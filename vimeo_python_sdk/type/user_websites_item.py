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


class RequiredUserWebsitesItem(TypedDict):
    # The website's description.
    description: typing.Optional[str]

    # The URL of the website.
    link: str

    # The name of the website.
    name: typing.Optional[str]

    # The URL type of the website.
    type: str

    # The URI of the custom website or social media page belonging to the user.
    uri: str

class OptionalUserWebsitesItem(TypedDict, total=False):
    pass

class UserWebsitesItem(RequiredUserWebsitesItem, OptionalUserWebsitesItem):
    pass

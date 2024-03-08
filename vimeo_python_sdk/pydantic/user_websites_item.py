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


class UserWebsitesItem(BaseModel):
    # The website's description.
    description: typing.Optional[str] = Field(alias='description')

    # The URL of the website.
    link: str = Field(alias='link')

    # The name of the website.
    name: typing.Optional[str] = Field(alias='name')

    # The URL type of the website.
    type: str = Field(alias='type')

    # The URI of the custom website or social media page belonging to the user.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

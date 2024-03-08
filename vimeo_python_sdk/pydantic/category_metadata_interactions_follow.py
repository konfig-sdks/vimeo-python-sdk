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


class CategoryMetadataInteractionsFollow(BaseModel):
    # Whether the authenticated user has followed the category.
    added: bool = Field(alias='added')

    # The time in ISO 8601 format when the user followed the category, or the null value if the user hasn't followed the category.
    added_time: typing.Optional[str] = Field(alias='added_time')

    # The URI for following or unfollowing the category: PUT to this URI to follow the category, or DELETE to this URI to unfollow the category.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

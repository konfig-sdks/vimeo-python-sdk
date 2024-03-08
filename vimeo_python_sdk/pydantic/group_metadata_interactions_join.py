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


class GroupMetadataInteractionsJoin(BaseModel):
    # The user's title. If this field isn't applicable, it takes the null value. This data requires a bearer token with the `private` scope.
    title: typing.Optional[str] = Field(alias='title')

    # Whether the user has followed the group. This data requires a bearer token with the `private` scope.
    added: bool = Field(alias='added')

    # The time in ISO 8601 format when the user joined the group. This data requires a bearer token with the `private` scope.
    added_time: typing.Optional[str] = Field(alias='added_time')

    # Whether the user is a moderator or subscriber. This data requires a bearer token with the `private` scope.  Option descriptions:  * `member` - The user is a member.  * `moderator` - The user is a moderator. 
    type: Literal["member", "moderator"] = Field(alias='type')

    # The URI for following the group. PUT to this URI to follow the group, or DELETE to this URI to unfollow the group. This data requires a bearer token with the `private` scope.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

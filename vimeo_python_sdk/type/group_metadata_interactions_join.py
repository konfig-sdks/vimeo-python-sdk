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


class RequiredGroupMetadataInteractionsJoin(TypedDict):
    # The user's title. If this field isn't applicable, it takes the null value. This data requires a bearer token with the `private` scope.
    title: typing.Optional[str]

    # Whether the user has followed the group. This data requires a bearer token with the `private` scope.
    added: bool

    # The time in ISO 8601 format when the user joined the group. This data requires a bearer token with the `private` scope.
    added_time: typing.Optional[str]

    # Whether the user is a moderator or subscriber. This data requires a bearer token with the `private` scope.  Option descriptions:  * `member` - The user is a member.  * `moderator` - The user is a moderator. 
    type: typing.Optional[str]

    # The URI for following the group. PUT to this URI to follow the group, or DELETE to this URI to unfollow the group. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalGroupMetadataInteractionsJoin(TypedDict, total=False):
    pass

class GroupMetadataInteractionsJoin(RequiredGroupMetadataInteractionsJoin, OptionalGroupMetadataInteractionsJoin):
    pass

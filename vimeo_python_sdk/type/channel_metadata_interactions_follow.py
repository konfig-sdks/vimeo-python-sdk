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


class RequiredChannelMetadataInteractionsFollow(TypedDict):
    # Whether the authenticated user has followed this channel. This data requires a bearer token with the `private` scope.
    added: bool

    # The time in ISO 8601 format that the user followed this channel, or the null value if the user hasn't followed the channel. This data requires a bearer token with the `private` scope.
    added_time: typing.Optional[str]

    # Whether the authenticated user is a moderator or subscriber. This data requires a bearer token with the `private` scope.  Option descriptions:  * `moderator` - The authenticated user is a moderator.  * `subscriber` - The authenticated user is a subscriber. 
    type: typing.Optional[str]

    # The URI for following or unfollowing this channel. PUT to this URI to follow the channel, or DELETE to this URI to unfollow the channel. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalChannelMetadataInteractionsFollow(TypedDict, total=False):
    pass

class ChannelMetadataInteractionsFollow(RequiredChannelMetadataInteractionsFollow, OptionalChannelMetadataInteractionsFollow):
    pass

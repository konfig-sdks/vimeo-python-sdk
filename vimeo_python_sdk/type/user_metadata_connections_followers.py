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

from vimeo_python_sdk.type.user_metadata_connections_followers_options import UserMetadataConnectionsFollowersOptions

class RequiredUserMetadataConnectionsFollowers(TypedDict):
    options: UserMetadataConnectionsFollowersOptions

    # The total number of followers on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalUserMetadataConnectionsFollowers(TypedDict, total=False):
    pass

class UserMetadataConnectionsFollowers(RequiredUserMetadataConnectionsFollowers, OptionalUserMetadataConnectionsFollowers):
    pass

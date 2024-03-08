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

from vimeo_python_sdk.type.user_metadata_connections_watchlater_options import UserMetadataConnectionsWatchlaterOptions

class RequiredUserMetadataConnectionsWatchlater(TypedDict):
    options: UserMetadataConnectionsWatchlaterOptions

    # The total number of videos on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalUserMetadataConnectionsWatchlater(TypedDict, total=False):
    pass

class UserMetadataConnectionsWatchlater(RequiredUserMetadataConnectionsWatchlater, OptionalUserMetadataConnectionsWatchlater):
    pass

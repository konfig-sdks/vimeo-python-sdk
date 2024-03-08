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

from vimeo_python_sdk.type.user_metadata_connections_shared_options import UserMetadataConnectionsSharedOptions

class RequiredUserMetadataConnectionsShared(TypedDict):
    options: UserMetadataConnectionsSharedOptions

    # The total number of videos on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalUserMetadataConnectionsShared(TypedDict, total=False):
    pass

class UserMetadataConnectionsShared(RequiredUserMetadataConnectionsShared, OptionalUserMetadataConnectionsShared):
    pass

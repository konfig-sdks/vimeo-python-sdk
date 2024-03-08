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

from vimeo_python_sdk.type.user_metadata_connections_connected_apps_options import UserMetadataConnectionsConnectedAppsOptions

class RequiredUserMetadataConnectionsConnectedApps(TypedDict):
    options: UserMetadataConnectionsConnectedAppsOptions

    # The total number of connected apps on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalUserMetadataConnectionsConnectedApps(TypedDict, total=False):
    pass

class UserMetadataConnectionsConnectedApps(RequiredUserMetadataConnectionsConnectedApps, OptionalUserMetadataConnectionsConnectedApps):
    pass

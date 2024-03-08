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

from vimeo_python_sdk.pydantic.user_metadata_interactions_connected_apps_options import UserMetadataInteractionsConnectedAppsOptions

class UserMetadataInteractionsConnectedApps(BaseModel):
    # The list of all the scopes on the connected app that are needed for a particular Vimeo feature.
    all_scopes: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='all_scopes')

    # Whether the authenticated user is connected to the connected app.
    is_connected: bool = Field(alias='is_connected')

    # The list of the remaining scopes on the connected app that the authenticated user needs for a particular Vimeo feature.
    needed_scopes: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='needed_scopes')

    options: UserMetadataInteractionsConnectedAppsOptions = Field(alias='options')

    # The URI of the connected app.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

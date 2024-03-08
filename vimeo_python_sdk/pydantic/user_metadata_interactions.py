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

from vimeo_python_sdk.pydantic.user_metadata_interactions_add_privacy_user import UserMetadataInteractionsAddPrivacyUser
from vimeo_python_sdk.pydantic.user_metadata_interactions_block import UserMetadataInteractionsBlock
from vimeo_python_sdk.pydantic.user_metadata_interactions_connected_apps import UserMetadataInteractionsConnectedApps
from vimeo_python_sdk.pydantic.user_metadata_interactions_follow import UserMetadataInteractionsFollow
from vimeo_python_sdk.pydantic.user_metadata_interactions_report import UserMetadataInteractionsReport

class UserMetadataInteractions(BaseModel):
    block: UserMetadataInteractionsBlock = Field(alias='block')

    connected_apps: UserMetadataInteractionsConnectedApps = Field(alias='connected_apps')

    follow: UserMetadataInteractionsFollow = Field(alias='follow')

    report: UserMetadataInteractionsReport = Field(alias='report')

    add_privacy_user: typing.Optional[UserMetadataInteractionsAddPrivacyUser] = Field(None, alias='add_privacy_user')
    class Config:
        arbitrary_types_allowed = True

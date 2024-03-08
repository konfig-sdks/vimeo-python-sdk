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

from vimeo_python_sdk.pydantic.user_metadata_interactions_block_options import UserMetadataInteractionsBlockOptions

class UserMetadataInteractionsBlock(BaseModel):
    # Whether the authenticated user is blocking the requested user.
    added: bool = Field(alias='added')

    # The time in ISO 8601 format when the block occurred, or the null value if no block exists.
    added_time: typing.Optional[str] = Field(alias='added_time')

    options: UserMetadataInteractionsBlockOptions = Field(alias='options')

    # The URI to block or unblock the requested user.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

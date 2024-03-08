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

from vimeo_python_sdk.type.user_metadata_interactions_block_options import UserMetadataInteractionsBlockOptions

class RequiredUserMetadataInteractionsBlock(TypedDict):
    # Whether the authenticated user is blocking the requested user.
    added: bool

    # The time in ISO 8601 format when the block occurred, or the null value if no block exists.
    added_time: typing.Optional[str]

    options: UserMetadataInteractionsBlockOptions

    # The URI to block or unblock the requested user.
    uri: str

class OptionalUserMetadataInteractionsBlock(TypedDict, total=False):
    pass

class UserMetadataInteractionsBlock(RequiredUserMetadataInteractionsBlock, OptionalUserMetadataInteractionsBlock):
    pass

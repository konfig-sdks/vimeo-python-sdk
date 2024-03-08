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


class RequiredCategoryMetadataInteractionsFollow(TypedDict):
    # Whether the authenticated user has followed the category.
    added: bool

    # The time in ISO 8601 format when the user followed the category, or the null value if the user hasn't followed the category.
    added_time: typing.Optional[str]

    # The URI for following or unfollowing the category: PUT to this URI to follow the category, or DELETE to this URI to unfollow the category.
    uri: str

class OptionalCategoryMetadataInteractionsFollow(TypedDict, total=False):
    pass

class CategoryMetadataInteractionsFollow(RequiredCategoryMetadataInteractionsFollow, OptionalCategoryMetadataInteractionsFollow):
    pass

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


class RequiredOnDemandVideoMetadataInteractionsLikes(TypedDict):
    # Whether the authenticated user has liked the video.
    added: bool

    # The time in ISO 8601 format when the authenticated user liked the video.
    added_time: str

    # The URI for the authenticated user to like the video.
    uri: str

class OptionalOnDemandVideoMetadataInteractionsLikes(TypedDict, total=False):
    pass

class OnDemandVideoMetadataInteractionsLikes(RequiredOnDemandVideoMetadataInteractionsLikes, OptionalOnDemandVideoMetadataInteractionsLikes):
    pass

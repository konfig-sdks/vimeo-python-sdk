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


class OnDemandVideoMetadataInteractionsWatchlater(BaseModel):
    # Whether the authenticated user has added the video to their Watch Later queue.
    added: bool = Field(alias='added')

    # The time in ISO 8601 format when the authenticated user added the video to their Watch Later queue.
    added_time: str = Field(alias='added_time')

    # The URI for the authenticated user to add the video to their Watch Later queue.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.picture import Picture

class ReplyMetadataConnectionsUser(BaseModel):
    # The absolute URL of the authenticated users's profile page.
    link: str = Field(alias='link')

    # The display name of the user who posted the reply.
    name: str = Field(alias='name')

    # Information about the user's portraits.
    pictures: Picture = Field(alias='pictures')

    # The unique identifier to access the user resource.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

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


class VideosCreditsAddUserCreditRequest(BaseModel):
    # The email address of the credited person.
    email: str = Field(alias='email')

    # The name of the credited person.
    name: str = Field(alias='name')

    # The role of the credited person.
    role: str = Field(alias='role')

    # The Vimeo URI of the credited person.
    user_uri: str = Field(alias='user_uri')
    class Config:
        arbitrary_types_allowed = True

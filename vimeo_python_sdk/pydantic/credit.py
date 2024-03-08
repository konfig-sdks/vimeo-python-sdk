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

from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.video import Video

class Credit(BaseModel):
    # The name of the person credited.
    name: str = Field(alias='name')

    # The character that the person portrayed, or the job that the person performed.
    role: str = Field(alias='role')

    # The unique identifier to access the credit resource.
    uri: str = Field(alias='uri')

    # The Vimeo user associated with the credit.
    user: typing.Optional[User] = Field(None, alias='user')

    # The video associated with the credit.
    video: typing.Optional[Video] = Field(None, alias='video')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.reply_metadata import ReplyMetadata

class Reply(BaseModel):
    # The time in ISO 8601 format when the reply was posted.
    created_on: str = Field(alias='created_on')

    # The permalink to the reply.
    link: str = Field(alias='link')

    metadata: ReplyMetadata = Field(alias='metadata')

    # The comment's resource key string.
    resource_key: str = Field(alias='resource_key')

    # The content of the reply.
    text: str = Field(alias='text')

    # The Vimeo content to which the reply relates.  Option descriptions:  * `video` - The comment is about a video. 
    type: Literal["video"] = Field(alias='type')

    # The unique identifier to access the reply resource.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.comment_metadata import CommentMetadata
from vimeo_python_sdk.pydantic.reply import Reply
from vimeo_python_sdk.pydantic.user import User

class Comment(BaseModel):
    # The time in ISO 8601 format when the comment was posted.
    created_on: str = Field(alias='created_on')

    # The permalink to the comment.
    link: str = Field(alias='link')

    metadata: CommentMetadata = Field(alias='metadata')

    # The list of replies to the comment.
    replies: typing.List[Reply] = Field(alias='replies')

    # The comment's resource key string.
    resource_key: str = Field(alias='resource_key')

    # The content of the comment.
    text: str = Field(alias='text')

    # The Vimeo content to which the comment relates.  Option descriptions:  * `video` - The comment is about a video. 
    type: Literal["video"] = Field(alias='type')

    # The unique identifier to access the comment resource.
    uri: str = Field(alias='uri')

    # The user who posted the comment. _This field is deprecated. Use the `metadata.connections.user` field instead._
    user: User = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True

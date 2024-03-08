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

from vimeo_python_sdk.type.comment_metadata import CommentMetadata
from vimeo_python_sdk.type.reply import Reply
from vimeo_python_sdk.type.user import User

class RequiredComment(TypedDict):
    # The time in ISO 8601 format when the comment was posted.
    created_on: str

    # The permalink to the comment.
    link: str

    metadata: CommentMetadata

    # The list of replies to the comment.
    replies: typing.List[Reply]

    # The comment's resource key string.
    resource_key: str

    # The content of the comment.
    text: str

    # The Vimeo content to which the comment relates.  Option descriptions:  * `video` - The comment is about a video. 
    type: str

    # The unique identifier to access the comment resource.
    uri: str

    # The user who posted the comment. _This field is deprecated. Use the `metadata.connections.user` field instead._
    user: User

class OptionalComment(TypedDict, total=False):
    pass

class Comment(RequiredComment, OptionalComment):
    pass

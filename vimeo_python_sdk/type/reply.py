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

from vimeo_python_sdk.type.reply_metadata import ReplyMetadata

class RequiredReply(TypedDict):
    # The time in ISO 8601 format when the reply was posted.
    created_on: str

    # The permalink to the reply.
    link: str

    metadata: ReplyMetadata

    # The comment's resource key string.
    resource_key: str

    # The content of the reply.
    text: str

    # The Vimeo content to which the reply relates.  Option descriptions:  * `video` - The comment is about a video. 
    type: str

    # The unique identifier to access the reply resource.
    uri: str

class OptionalReply(TypedDict, total=False):
    pass

class Reply(RequiredReply, OptionalReply):
    pass

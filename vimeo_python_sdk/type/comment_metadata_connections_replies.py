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

from vimeo_python_sdk.type.comment_metadata_connections_replies_options import CommentMetadataConnectionsRepliesOptions

class RequiredCommentMetadataConnectionsReplies(TypedDict):
    options: CommentMetadataConnectionsRepliesOptions

    # The total number of replies on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalCommentMetadataConnectionsReplies(TypedDict, total=False):
    pass

class CommentMetadataConnectionsReplies(RequiredCommentMetadataConnectionsReplies, OptionalCommentMetadataConnectionsReplies):
    pass

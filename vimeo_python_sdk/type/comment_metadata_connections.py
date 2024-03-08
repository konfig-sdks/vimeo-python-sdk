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

from vimeo_python_sdk.type.comment_metadata_connections_replies import CommentMetadataConnectionsReplies
from vimeo_python_sdk.type.comment_metadata_connections_user import CommentMetadataConnectionsUser

class RequiredCommentMetadataConnections(TypedDict):
    replies: CommentMetadataConnectionsReplies

    user: CommentMetadataConnectionsUser

class OptionalCommentMetadataConnections(TypedDict, total=False):
    pass

class CommentMetadataConnections(RequiredCommentMetadataConnections, OptionalCommentMetadataConnections):
    pass

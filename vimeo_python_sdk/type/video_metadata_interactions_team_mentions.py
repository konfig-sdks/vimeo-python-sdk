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

from vimeo_python_sdk.type.video_metadata_interactions_team_mentions_options import VideoMetadataInteractionsTeamMentionsOptions

class RequiredVideoMetadataInteractionsTeamMentions(TypedDict):
    options: VideoMetadataInteractionsTeamMentionsOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsTeamMentions(TypedDict, total=False):
    pass

class VideoMetadataInteractionsTeamMentions(RequiredVideoMetadataInteractionsTeamMentions, OptionalVideoMetadataInteractionsTeamMentions):
    pass

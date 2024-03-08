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

from vimeo_python_sdk.type.channels_tags_add_multiple_tags_to_channel_request_tag import ChannelsTagsAddMultipleTagsToChannelRequestTag

class RequiredChannelsTagsAddMultipleTagsToChannelRequest(TypedDict):
    tag: ChannelsTagsAddMultipleTagsToChannelRequestTag

class OptionalChannelsTagsAddMultipleTagsToChannelRequest(TypedDict, total=False):
    pass

class ChannelsTagsAddMultipleTagsToChannelRequest(RequiredChannelsTagsAddMultipleTagsToChannelRequest, OptionalChannelsTagsAddMultipleTagsToChannelRequest):
    pass

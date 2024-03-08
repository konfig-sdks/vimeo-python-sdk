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

from vimeo_python_sdk.type.category import Category
from vimeo_python_sdk.type.channel_metadata import ChannelMetadata
from vimeo_python_sdk.type.channel_privacy import ChannelPrivacy
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.tag import Tag
from vimeo_python_sdk.type.user import User

class RequiredChannel(TypedDict):
    # An array of all tags assigned to the channel.
    tags: typing.List[Tag]

    # A brief explanation of the channel's content.
    description: typing.Optional[str]

    # The categories to which the channel belongs as specified by the channel moderators.
    categories: typing.List[Category]

    # The time in ISO 8601 format when the channel was created.
    created_time: str

    # The banner that appears by default at the top of the channel page.
    header: Picture

    # The URL to access the channel in a browser.
    link: str

    metadata: ChannelMetadata

    # The time in ISO 8601 format when the channel was last modified.
    modified_time: str

    # The display name that identifies the channel.
    name: str

    # The active image for the channel. The default is the thumbnail of the last video added to the channel.
    pictures: Picture

    privacy: ChannelPrivacy

    # The channel resource key.
    resource_key: str

    # The unique identifier to access the channel resource.
    uri: str

    # The Vimeo user who owns the channel.
    user: User

class OptionalChannel(TypedDict, total=False):
    pass

class Channel(RequiredChannel, OptionalChannel):
    pass

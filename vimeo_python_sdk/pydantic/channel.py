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

from vimeo_python_sdk.pydantic.category import Category
from vimeo_python_sdk.pydantic.channel_metadata import ChannelMetadata
from vimeo_python_sdk.pydantic.channel_privacy import ChannelPrivacy
from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.tag import Tag
from vimeo_python_sdk.pydantic.user import User

class Channel(BaseModel):
    # An array of all tags assigned to the channel.
    tags: typing.List[Tag] = Field(alias='tags')

    # A brief explanation of the channel's content.
    description: typing.Optional[str] = Field(alias='description')

    # The categories to which the channel belongs as specified by the channel moderators.
    categories: typing.List[Category] = Field(alias='categories')

    # The time in ISO 8601 format when the channel was created.
    created_time: str = Field(alias='created_time')

    # The banner that appears by default at the top of the channel page.
    header: Picture = Field(alias='header')

    # The URL to access the channel in a browser.
    link: str = Field(alias='link')

    metadata: ChannelMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the channel was last modified.
    modified_time: str = Field(alias='modified_time')

    # The display name that identifies the channel.
    name: str = Field(alias='name')

    # The active image for the channel. The default is the thumbnail of the last video added to the channel.
    pictures: Picture = Field(alias='pictures')

    privacy: ChannelPrivacy = Field(alias='privacy')

    # The channel resource key.
    resource_key: str = Field(alias='resource_key')

    # The unique identifier to access the channel resource.
    uri: str = Field(alias='uri')

    # The Vimeo user who owns the channel.
    user: User = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True

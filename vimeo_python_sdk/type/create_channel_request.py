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


class RequiredCreateChannelRequest(TypedDict):
    # The name of the channel.
    name: str

    # The privacy level of the channel.  Option descriptions:  * `anybody` - Anyone can access the channel.  * `moderators` - Only moderators can access the channel.  * `user` - Only moderators and designated users can access the channel. 
    privacy: str

class OptionalCreateChannelRequest(TypedDict, total=False):
    # The description of the channel.
    description: str

    # The link to access the channel. You can use a custom name in the URL in place of a numeric channel ID, as in `/channels/{url_custom}`.
    link: str

class CreateChannelRequest(RequiredCreateChannelRequest, OptionalCreateChannelRequest):
    pass

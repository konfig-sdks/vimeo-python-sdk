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


class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamEmbed(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamEmbed(TypedDict, total=False):
    # The embed permission level for the event.  Option descriptions:  * `private` - Only the user can embed the event.  * `public` - Anyone can embed the event.  * `whitelist` - Only those on the whitelist can embed the event. 
    embed: str

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamEmbed(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamEmbed, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1StreamEmbed):
    pass

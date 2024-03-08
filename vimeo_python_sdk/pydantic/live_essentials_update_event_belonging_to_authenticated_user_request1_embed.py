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

from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request1_embed_logos import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogos

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1Embed(BaseModel):
    # Whether playback starts automatically on load.
    autoplay: typing.Optional[bool] = Field(None, alias='autoplay')

    # The hexadecimal color code for the main color of the embed player.
    color: typing.Optional[str] = Field(None, alias='color')

    logos: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogos] = Field(None, alias='logos')

    # Whether the playlist should start from the beginning again after reaching the end of the last video.
    loop: typing.Optional[bool] = Field(None, alias='loop')

    # Whether to show the playlist controls on the embed player.
    playlist: typing.Optional[bool] = Field(None, alias='playlist')

    # Whether to show the event schedule on the embed player.
    schedule: typing.Optional[bool] = Field(None, alias='schedule')

    # Whether the embed player should use (`true`) or ignore (`false`) the **embed.color** value.
    use_color: typing.Optional[bool] = Field(None, alias='use_color')
    class Config:
        arbitrary_types_allowed = True

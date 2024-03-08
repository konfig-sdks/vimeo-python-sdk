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


class LiveEventDestination(BaseModel):
    # The name of the destination target, whether a page, profile name, or the like.
    display_name: str = Field(alias='display_name')

    # The ID of the destination.
    id: typing.Union[int, float] = Field(alias='id')

    # Whether the destination is enabled.
    is_enabled: bool = Field(alias='is_enabled')

    # The ID of the live video.
    live_clip_id: typing.Union[int, float] = Field(alias='live_clip_id')

    # The privacy setting of the destination.  Option descriptions:  * `CONNECTIONS` - The privacy setting is `CONNECTIONS` for LinkedIn.  * `PUBLIC` - The privacy setting is `PUBLIC` for LinkedIn.  * `all_friends` - The privacy setting is `all_friends` for Facebook.  * `everyone` - The privacy setting is `everyone` for Facebook.  * `private` - The privacy setting is `private` for YouTube.  * `public` - The privacy setting is `public` for YouTube.  * `self` - The privacy setting is `self` for Facebook.  * `unlisted` - The privacy setting is `unlisted` for YouTube. 
    privacy: Literal["CONNECTIONS", "PUBLIC", "all_friends", "everyone", "private", "public", "self", "unlisted"] = Field(alias='privacy')

    # The destination ID of the destination service.
    provider_broadcast_id: typing.Optional[str] = Field(alias='provider_broadcast_id')

    # The broadcast ID of the destination service.
    provider_destination_id: typing.Optional[str] = Field(alias='provider_destination_id')

    # The user ID of the destination service.
    provider_user_id: typing.Optional[str] = Field(alias='provider_user_id')

    # The ID of the scheduled live video.
    provider_video_id: typing.Optional[str] = Field(alias='provider_video_id')

    # The time in Unix timestamp format when live streaming is scheduled to start.
    scheduled_at: typing.Optional[typing.Union[int, float]] = Field(alias='scheduled_at')

    # The name of the destination service.  Option descriptions:  * `custom_rtmp` - The destination service is custom RTMP.  * `facebook` - The destination service is Facebook Live.  * `linkedin` - The destination service is LinkedIn Live.  * `youtube` - The destination service is YouTube Live. 
    service_name: Literal["custom_rtmp", "facebook", "linkedin", "youtube"] = Field(alias='service_name')

    # The status of the destination.  Option descriptions:  * `0` - The status is OK.  * `1` - An error occurred. Check the `state_message` field for details. 
    state: Literal["0", "1"] = Field(alias='state')

    # The message that describes the state of the destination.
    state_message: typing.Optional[str] = Field(alias='state_message')

    # The stream key for the simulcast destination.
    stream_key: typing.Optional[str] = Field(alias='stream_key')

    # The RTMP URL to stream to.
    stream_url: typing.Optional[str] = Field(alias='stream_url')

    # The type of the simulcast destination.  Option descriptions:  * `channel` - The destination is a YouTube channel.  * `custom` - The destination is custom.  * `organization` - The destination is a LinkedIn organization.  * `page` - The destination is a Facebook page.  * `profile` - The destination is a Facebook or LinkedIn profile. 
    type: Literal["channel", "custom", "organization", "page", "profile"] = Field(alias='type')

    # The ID of the destination's owner.
    user_id: typing.Union[int, float] = Field(alias='user_id')
    class Config:
        arbitrary_types_allowed = True

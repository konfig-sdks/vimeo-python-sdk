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


class LiveEventDestinationsCreateOneTimeLiveEventDestinationRequest(BaseModel):
    # The title to display for the simulcast.
    display_name: str = Field(alias='display_name')

    # The service to simulcast to.  Option descriptions:  * `custom_rtmp` - Simulcast to a custom service.  * `facebook` - Simulcast to Facebook Live.  * `linkedin` - Simulcast to LinkedIn Live.  * `youtube` - Simulcast to YouTube Live. 
    service_name: Literal["custom_rtmp", "facebook", "linkedin", "youtube"] = Field(alias='service_name')

    # The type of the simulcast destination.  Option descriptions:  * `channel` - The destination is a YouTube channel.  * `custom` - The destination is custom.  * `organization` - The destination is a LinkedIn organization.  * `page` - The destination is a Facebook page.  * `profile` - The destination is a Facebook or LinkedIn profile. 
    type: Literal["channel", "custom", "organization", "page", "profile"] = Field(alias='type')

    # Whether the destination is enabled for simulcasting.
    is_enabled: typing.Optional[bool] = Field(None, alias='is_enabled')

    # The privacy setting of the destination. Be sure to choose a value that corresponds to your service.  Option descriptions:  * `CONNECTIONS` - The privacy setting is `CONNECTIONS` for LinkedIn.  * `PUBLIC` - The privacy setting is `PUBLIC` for LinkedIn.  * `all_friends` - The privacy setting is `all_friends` for Facebook.  * `everyone` - The privacy setting is `everyone` for Facebook.  * `private` - The privacy setting is `private` for YouTube.  * `public` - The privacy setting is `public` for YouTube.  * `self` - The privacy setting is `self` for Facebook.  * `unlisted` - The privacy setting is `unlisted` for YouTube. 
    privacy: typing.Optional[Literal["CONNECTIONS", "PUBLIC", "all_friends", "everyone", "private", "public", "self", "unlisted"]] = Field(None, alias='privacy')

    # The ID of the destination on the specified service, such as the YouTube channel ID or the Facebook page ID.
    provider_destination_id: typing.Optional[str] = Field(None, alias='provider_destination_id')

    # The ID of the scheduled video.
    provider_video_id: typing.Optional[typing.Optional[str]] = Field(None, alias='provider_video_id')

    # The time in Unix timestamp format when live streaming is scheduled to start.
    scheduled_at: typing.Optional[typing.Union[int, float]] = Field(None, alias='scheduled_at')

    # The RTMP stream key.
    stream_key: typing.Optional[str] = Field(None, alias='stream_key')

    # The RTMP URL for receiving the video stream.
    stream_url: typing.Optional[str] = Field(None, alias='stream_url')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.live_essentials_create_event_for_user_request_content_rating import LiveEssentialsCreateEventForUserRequestContentRating
from vimeo_python_sdk.pydantic.live_essentials_create_event_for_user_request_embed import LiveEssentialsCreateEventForUserRequestEmbed
from vimeo_python_sdk.pydantic.live_essentials_create_event_for_user_request_interaction_tools_settings import LiveEssentialsCreateEventForUserRequestInteractionToolsSettings
from vimeo_python_sdk.pydantic.live_essentials_create_event_for_user_request_schedule import LiveEssentialsCreateEventForUserRequestSchedule
from vimeo_python_sdk.pydantic.live_essentials_create_event_for_user_request_stream_embed import LiveEssentialsCreateEventForUserRequestStreamEmbed
from vimeo_python_sdk.pydantic.live_essentials_create_event_for_user_request_stream_privacy import LiveEssentialsCreateEventForUserRequestStreamPrivacy

class LiveEssentialsCreateEventForUserRequest(BaseModel):
    # The title of the event. If **automatically_title_stream** is `true`, this value is the base title for videos created by streaming to this event.
    title: str = Field(alias='title')

    # Whether the share link is usable.
    allow_share_link: typing.Optional[bool] = Field(None, alias='allow_share_link')

    # Whether automated closed captions are enabled for the event.
    auto_cc_enabled: typing.Optional[bool] = Field(None, alias='auto_cc_enabled')

    # A comma-separated list of keywords that improve the quality of the automated closed captions.
    auto_cc_keywords: typing.Optional[str] = Field(None, alias='auto_cc_keywords')

    # The language in which the automated closed captions appear.  Option descriptions:  * `de-DE` - The language is German.  * `en-US` - The language is English.  * `es-ES` - The language is Spanish.  * `fr-FR` - The language is French.  * `pt-BR` - The language is Portuguese. 
    auto_cc_lang: typing.Optional[Literal["de-DE", "en-US", "es-ES", "fr-FR", "pt-BR"]] = Field(None, alias='auto_cc_lang')

    # Whether the title for the next video in the event is generated based on the time of the stream and the **title** field of the event.
    automatically_title_stream: typing.Optional[bool] = Field(None, alias='automatically_title_stream')

    # Whether to display the live chat client on the Vimeo event page.
    chat_enabled: typing.Optional[bool] = Field(None, alias='chat_enabled')

    content_rating: typing.Optional[LiveEssentialsCreateEventForUserRequestContentRating] = Field(None, alias='content_rating')

    # Whether the DVR feature is enabled.
    dvr: typing.Optional[bool] = Field(None, alias='dvr')

    embed: typing.Optional[LiveEssentialsCreateEventForUserRequestEmbed] = Field(None, alias='embed')

    # The URI of the event's folder.
    folder_uri: typing.Optional[str] = Field(None, alias='folder_uri')

    interaction_tools_settings: typing.Optional[LiveEssentialsCreateEventForUserRequestInteractionToolsSettings] = Field(None, alias='interaction_tools_settings')

    # Whether the event has low-latency streaming enabled.
    low_latency: typing.Optional[bool] = Field(None, alias='low_latency')

    # The order in which the videos of the event appear within the event's playlist.  Option descriptions:  * `added_first` - The most recently added videos appear first.  * `added_last` - The most recently added videos appear last.  * `alphabetical` - The videos appear in alphabetical order.  * `arranged` - The videos appear in the order in which the user has arranged them.  * `comments` - The videos appear in order of number of comments.  * `duration` - The videos appear in order of duration.  * `likes` - The videos appear in order of number of likes.  * `newest` - The newest videos appear first.  * `oldest` - The oldest videos appear first.  * `plays` - The videos appear in order of number of plays. 
    playlist_sort: typing.Optional[Literal["added_first", "added_last", "alphabetical", "arranged", "comments", "duration", "likes", "newest", "oldest", "plays"]] = Field(None, alias='playlist_sort')

    # Whether the event has RTMP preview enabled.
    rtmp_preview: typing.Optional[bool] = Field(None, alias='rtmp_preview')

    schedule: typing.Optional[LiveEssentialsCreateEventForUserRequestSchedule] = Field(None, alias='schedule')

    # Whether the scheduled playback feature is enabled.
    scheduled_playback: typing.Optional[bool] = Field(None, alias='scheduled_playback')

    # The description of the next video to be streamed to the event.
    stream_description: typing.Optional[str] = Field(None, alias='stream_description')

    stream_embed: typing.Optional[LiveEssentialsCreateEventForUserRequestStreamEmbed] = Field(None, alias='stream_embed')

    # The password when **stream_privacy.view** is `password`. Anyone with the password can view the videos generated by streaming to the event.
    stream_password: typing.Optional[str] = Field(None, alias='stream_password')

    stream_privacy: typing.Optional[LiveEssentialsCreateEventForUserRequestStreamPrivacy] = Field(None, alias='stream_privacy')

    # The title of the next video to be streamed to the event. This parameter is required when **automatically_title_stream** is `false`.
    stream_title: typing.Optional[str] = Field(None, alias='stream_title')

    # The time zone used in resolving the timestamps that are included in automatically generated video titles.
    time_zone: typing.Optional[str] = Field(None, alias='time_zone')
    class Config:
        arbitrary_types_allowed = True

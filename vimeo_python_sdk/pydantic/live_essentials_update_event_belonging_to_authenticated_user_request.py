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

from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_content_rating import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_interaction_tools_settings import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_schedule import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_stream_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed
from vimeo_python_sdk.pydantic.live_essentials_update_event_belonging_to_authenticated_user_request_stream_privacy import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest(BaseModel):
    # The title of the event. If **automatically_title_stream** is `true`, this value is the base title for videos created by streaming to this event.
    title: typing.Optional[str] = Field(None, alias='title')

    # Whether automated closed captions are enabled for the event.
    auto_cc_enabled: typing.Optional[bool] = Field(None, alias='auto_cc_enabled')

    # A comma-separated list of keywords for enhancing the speech detection of automated closed captions.
    auto_cc_keywords: typing.Optional[str] = Field(None, alias='auto_cc_keywords')

    # The language of the automated closed captions.  Option descriptions:  * `de-DE` - The language is German.  * `en-US` - The language is English.  * `es-ES` - The language is Spanish.  * `fr-FR` - The language is French.  * `pt-BR` - The language is Portuguese. 
    auto_cc_language: typing.Optional[Literal["de-DE", "en-US", "es-ES", "fr-FR", "pt-BR"]] = Field(None, alias='auto_cc_language')

    # Whether the title for the next video in the event is generated based on the time of the stream and the **title** field of the event.
    automatically_title_stream: typing.Optional[bool] = Field(None, alias='automatically_title_stream')

    # Whether to display the live chat client on the Vimeo event page.
    chat_enabled: typing.Optional[bool] = Field(None, alias='chat_enabled')

    content_rating: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating] = Field(None, alias='content_rating')

    # Whether the DVR feature is enabled.
    dvr: typing.Optional[bool] = Field(None, alias='dvr')

    embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed] = Field(None, alias='embed')

    interaction_tools_settings: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings] = Field(None, alias='interaction_tools_settings')

    # The order in which the videos of the event appear within the event's playlist.  Option descriptions:  * `added_first` - The most recently added videos appear first.  * `added_last` - The most recently added videos appear last.  * `alphabetical` - The videos appear in alphabetical order.  * `arranged` - The videos appear in the order in which the user has arranged them.  * `comments` - The videos appear in order of number of comments.  * `duration` - The videos appear in order of duration.  * `likes` - The videos appear in order of number of likes.  * `newest` - The newest videos appear first.  * `oldest` - The oldest videos appear first.  * `plays` - The videos appear in order of number of plays. 
    playlist_sort: typing.Optional[Literal["added_first", "added_last", "alphabetical", "arranged", "comments", "duration", "likes", "newest", "oldest", "plays"]] = Field(None, alias='playlist_sort')

    schedule: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule] = Field(None, alias='schedule')

    # Whether the scheduled playback feature is enabled.
    scheduled_playback: typing.Optional[bool] = Field(None, alias='scheduled_playback')

    # The description of the next video to be streamed to the event.
    stream_description: typing.Optional[str] = Field(None, alias='stream_description')

    stream_embed: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed] = Field(None, alias='stream_embed')

    # The stream mode of the event.  Option descriptions:  * `live` - The stream is live playback.  * `record` - The stream is in record mode.  * `simulive` - The stream is scheduled media playback. 
    stream_mode: typing.Optional[Literal["live", "record", "simulive"]] = Field(None, alias='stream_mode')

    # The password when **stream_privacy.view** is `password`. Anyone with the password can view the videos generated by streaming to the event.
    stream_password: typing.Optional[str] = Field(None, alias='stream_password')

    stream_privacy: typing.Optional[LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy] = Field(None, alias='stream_privacy')

    # The title of the next video to be streamed to the event. This parameter is required when **automatically_title_stream** is `false`.
    stream_title: typing.Optional[str] = Field(None, alias='stream_title')

    # The time zone used in resolving the timestamps that are included in automatically generated video titles.
    time_zone: typing.Optional[str] = Field(None, alias='time_zone')
    class Config:
        arbitrary_types_allowed = True

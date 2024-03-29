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

from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_content_rating import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_interaction_tools_settings import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_schedule import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_stream_embed import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed
from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_stream_privacy import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy

class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest(TypedDict, total=False):
    # The title of the event. If **automatically_title_stream** is `true`, this value is the base title for videos created by streaming to this event.
    title: str

    # Whether automated closed captions are enabled for the event.
    auto_cc_enabled: bool

    # A comma-separated list of keywords for enhancing the speech detection of automated closed captions.
    auto_cc_keywords: str

    # The language of the automated closed captions.  Option descriptions:  * `de-DE` - The language is German.  * `en-US` - The language is English.  * `es-ES` - The language is Spanish.  * `fr-FR` - The language is French.  * `pt-BR` - The language is Portuguese. 
    auto_cc_language: str

    # Whether the title for the next video in the event is generated based on the time of the stream and the **title** field of the event.
    automatically_title_stream: bool

    # Whether to display the live chat client on the Vimeo event page.
    chat_enabled: bool

    content_rating: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestContentRating

    # Whether the DVR feature is enabled.
    dvr: bool

    embed: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbed

    interaction_tools_settings: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestInteractionToolsSettings

    # The order in which the videos of the event appear within the event's playlist.  Option descriptions:  * `added_first` - The most recently added videos appear first.  * `added_last` - The most recently added videos appear last.  * `alphabetical` - The videos appear in alphabetical order.  * `arranged` - The videos appear in the order in which the user has arranged them.  * `comments` - The videos appear in order of number of comments.  * `duration` - The videos appear in order of duration.  * `likes` - The videos appear in order of number of likes.  * `newest` - The newest videos appear first.  * `oldest` - The oldest videos appear first.  * `plays` - The videos appear in order of number of plays. 
    playlist_sort: str

    schedule: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestSchedule

    # Whether the scheduled playback feature is enabled.
    scheduled_playback: bool

    # The description of the next video to be streamed to the event.
    stream_description: str

    stream_embed: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamEmbed

    # The stream mode of the event.  Option descriptions:  * `live` - The stream is live playback.  * `record` - The stream is in record mode.  * `simulive` - The stream is scheduled media playback. 
    stream_mode: str

    # The password when **stream_privacy.view** is `password`. Anyone with the password can view the videos generated by streaming to the event.
    stream_password: str

    stream_privacy: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestStreamPrivacy

    # The title of the next video to be streamed to the event. This parameter is required when **automatically_title_stream** is `false`.
    stream_title: str

    # The time zone used in resolving the timestamps that are included in automatically generated video titles.
    time_zone: str

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest):
    pass

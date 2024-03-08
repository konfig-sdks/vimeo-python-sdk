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

from vimeo_python_sdk.type.live_event_album import LiveEventAlbum
from vimeo_python_sdk.type.live_event_allowed_privacies import LiveEventAllowedPrivacies
from vimeo_python_sdk.type.live_event_content_rating import LiveEventContentRating
from vimeo_python_sdk.type.live_event_email_quota import LiveEventEmailQuota
from vimeo_python_sdk.type.live_event_embed import LiveEventEmbed
from vimeo_python_sdk.type.live_event_interaction_tools_settings import LiveEventInteractionToolsSettings
from vimeo_python_sdk.type.live_event_live_clips import LiveEventLiveClips
from vimeo_python_sdk.type.live_event_live_destinations import LiveEventLiveDestinations
from vimeo_python_sdk.type.live_event_metadata import LiveEventMetadata
from vimeo_python_sdk.type.live_event_schedule import LiveEventSchedule
from vimeo_python_sdk.type.live_event_stream_privacy import LiveEventStreamPrivacy
from vimeo_python_sdk.type.live_event_webinar import LiveEventWebinar
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.project import Project
from vimeo_python_sdk.type.user import User

class RequiredLiveEvent(TypedDict):
    # The title of the event. This field is also optionally used as the base title for videos created by streaming to the event.
    title: str

    album: LiveEventAlbum

    # Whether the share link for the videos generated by streaming to the event is usable.
    allow_share_link: bool

    allowed_privacies: LiveEventAllowedPrivacies

    # Whether the automated closed captions feature is enabled.
    auto_cc_enabled: typing.Optional[bool]

    # A comma-separated list of keywords for enhancing the speech detection of automated closed captions.
    auto_cc_keywords: typing.Optional[str]

    # The language of the automated closed captions.  Option descriptions:  * `de-DE` - The language is German.  * `en-US` - The language is English.  * `es-ES` - The language is Spanish.  * `fr-FR` - The language is French.  * `pt-BR` - The language is Portuguese. 
    auto_cc_language: typing.Optional[str]

    # The amount of time remaining to the user to access the automated closed captions feature.
    auto_cc_remaining: typing.Optional[typing.Union[int, float]]

    # When the value of this field is `true`, the title for the next video in the event is generated based on the time of the stream and the **title** field of the event.
    automatically_title_stream: bool

    # Whether to display live chat on the event page on Vimeo.
    chat_enabled: bool

    # The time in ISO 8601 format when the event was completed.
    completed_on: str

    content_rating: LiveEventContentRating

    # The time in ISO 8601 format when the event was created.
    created_time: str

    # Whether the DVR feature is enabled.
    dvr: bool

    email_quota: LiveEventEmailQuota

    embed: LiveEventEmbed

    # Whether the event was created from a showcase.
    from_showcase: bool

    # The first video to be played in the playlist.
    head_clip: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    interaction_tools_settings: LiveEventInteractionToolsSettings

    # The type of latency.  Option descriptions:  * `fail-safe` - The latency is in the failsafe range, with a delay of 60-75 seconds.  * `low` - The latency is low, with a delay of 5-7 seconds.  * `standard` - The latency is standard, with a delay of 15-20 seconds. 
    latency: str

    # The unique ID for the registered viewer.
    lead_uuid: str

    # The URI to access the event on Vimeo.
    link: str

    live_clips: LiveEventLiveClips

    live_destinations: LiveEventLiveDestinations

    # Whether the low-latency feature is enabled.
    low_latency: bool

    metadata: LiveEventMetadata

    # The date in ISO 8601 format on which the next occurrence of the event is expected to be live.
    next_occurrence_time: typing.Optional[str]

    # Information about the folder that contains the event.
    parent_folder: Project

    # The active thumbnail image of the event.
    pictures: Picture

    # The order in which the videos inside the event appear in the playlist.  Option descriptions:  * `added_first` - The videos appear according to when they were added to the event, with the most recently added first.  * `added_last` - The videos appear according to when they were added to the event, with the most recently added last.  * `alphabetical` - The videos appear alphabetically by their title.  * `arranged` - The videos appear as arranged by the owner of the event.  * `comments` - The videos appear according to their number of comments.  * `duration` - The videos appear in order of duration.  * `likes` - The videos appear according to their number of likes.  * `newest` - The videos appear in chronological order, with the newest first.  * `oldest` - The videos appear in chronological order, with the oldest first.  * `plays` - The videos appear according to their number of plays. 
    playlist_sort: str

    # The preferred streaming method.  Option descriptions:  * `browser` - Stream in the browser.  * `encoder` - Stream by the encoder. 
    preferred_stream_method: str

    # The upstream RTMP link. Send your live content to this link to create a live video on the event.
    rtmp_link: typing.Optional[str]

    # Whether to preview the RTMP stream before the event goes live.
    rtmp_preview: bool

    # The upstream RTMPS link. Send your live content to this link to create a live video on the event.
    rtmps_link: typing.Optional[str]

    # The description of the time or times that the event is expected to be live.
    schedule: LiveEventSchedule

    # Whether the scheduled playback feature is enabled.
    scheduled_playback: bool

    # The status of the event.  Option descriptions:  * `ended` - The user ended the event.  * `started` - The user started the event. 
    status: typing.Optional[str]

    # The description of the next video streamed to the event.
    stream_description: typing.Optional[str]

    # The stream key used in conjunction with the RTMP and RTMPS links.
    stream_key: typing.Optional[str]

    # The stream mode of the event.  Option descriptions:  * `live` - The stream is live playback.  * `record` - The stream is in record mode.  * `simulive` - The stream is scheduled media playback. 
    stream_mode: str

    # The password that anyone can use to access the videos generated by streaming to the event.
    stream_password: typing.Optional[str]

    stream_privacy: LiveEventStreamPrivacy

    # The title of the next video streamed to the event. This field applies only when **automatically_title_stream** is `false`.
    stream_title: str

    # The event's video. An event always has a video, which is either in a pre-live state (ready to be streamed to) or in a live state (which is currently being streamed to).
    streamable_clip: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # The time zone used in resolving the timestamps included in auto-generated video titles.
    time_zone: str

    # Whether to ignore the time limit of the automated closed captions feature.
    unlimited_auto_cc: typing.Optional[bool]

    # Whether 24/7 streaming is enabled for the event.
    unlimited_duration: bool

    # The event's canonical relative URI.
    uri: str

    # The owner of the event.
    user: User

    # The URI to access the event on Vimeo with or without an unlisted hash.
    view_link: str

    webinar: LiveEventWebinar

class OptionalLiveEvent(TypedDict, total=False):
    # Whether the event was created from a webinar.
    from_webinar: bool

class LiveEvent(RequiredLiveEvent, OptionalLiveEvent):
    pass

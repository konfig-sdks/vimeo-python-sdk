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

from vimeo_python_sdk.type.webinar_event_embed_available_player_logos import WebinarEventEmbedAvailablePlayerLogos
from vimeo_python_sdk.type.webinar_event_embed_colors import WebinarEventEmbedColors
from vimeo_python_sdk.type.webinar_event_embed_embed_properties import WebinarEventEmbedEmbedProperties
from vimeo_python_sdk.type.webinar_event_embed_logos import WebinarEventEmbedLogos

class RequiredWebinarEventEmbed(TypedDict):
    # Whether the embedded RLE player should display the video title.
    title: bool

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool

    # Whether the embedded RLE player should autoplay the RLE content.
    autoplay: bool

    available_player_logos: WebinarEventEmbedAvailablePlayerLogos

    # Whether the embedded RLE player should display the author's name.
    byline: bool

    # The chat's iFrame source URL.
    chat_embed_source: typing.Optional[str]

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color: str

    colors: WebinarEventEmbedColors

    # The embed code for RLE chat.
    embed_chat: typing.Optional[str]

    embed_properties: WebinarEventEmbedEmbedProperties

    # Whether the embedded RLE player should display the event schedule.
    event_schedule: bool

    # Whether the embedded RLE player should include the fullscreen controls.
    fullscreen_button: bool

    # Whether the Live label should be visible over the player.
    hide_live_label: bool

    # Whether the embedded RLE player should hide the viewer counter.
    hide_viewer_count: bool

    # The fixed HTML code to embed the event's playlist on a website.
    html: typing.Optional[str]

    # Whether the embedded RLE player should include the `like` button.
    like_button: bool

    logos: WebinarEventEmbedLogos

    # Whether the embedded RLE player should loop back to the first video once content is exhausted.
    loop: bool

    # Whether picture-in-picture is enabled and the button appears in the embeddable player.
    pip: bool

    # The position of the player's play button.  Option descriptions:  * `0` - The play button has the default position.  * `1` - The play button appears at the bottom of the interface.  * `2` - The play button appears in the center of the interface. 
    play_button_position: str

    # Whether the embedded RLE player should include the playbar.
    playbar: bool

    # Whether the playlist component appears in the embeddable player for this RLE.
    playlist: bool

    # Whether the embedded RLE player should display the author's portrait.
    portrait: bool

    # The responsive HTML code to embed the event's playlist on a website.
    responsive_html: typing.Optional[str]

    # Whether the schedule component appears in the embeddable player for this RLE.
    schedule: bool

    # Whether the embedded RLE player should display the latest video placeholder.
    show_latest_archived_clip: bool

    # Whether the embedded RLE player should display the schedule timezone.
    show_timezone: bool

    # Whether the embedded RLE player should use a custom color or the default Vimeo blue.
    use_color: str

    # Whether the embedded RLE player should include the volume controls.
    volume: bool

class OptionalWebinarEventEmbed(TypedDict, total=False):
    pass

class WebinarEventEmbed(RequiredWebinarEventEmbed, OptionalWebinarEventEmbed):
    pass

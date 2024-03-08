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

from vimeo_python_sdk.pydantic.live_event_recurring_embed_available_player_logos import LiveEventRecurringEmbedAvailablePlayerLogos
from vimeo_python_sdk.pydantic.live_event_recurring_embed_colors import LiveEventRecurringEmbedColors
from vimeo_python_sdk.pydantic.live_event_recurring_embed_embed_properties import LiveEventRecurringEmbedEmbedProperties
from vimeo_python_sdk.pydantic.live_event_recurring_embed_logos import LiveEventRecurringEmbedLogos

class LiveEventRecurringEmbed(BaseModel):
    # Whether the embedded RLE player should display the video title.
    title: bool = Field(alias='title')

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool = Field(alias='airplay')

    # Whether the embedded RLE player should autoplay the RLE content.
    autoplay: bool = Field(alias='autoplay')

    available_player_logos: LiveEventRecurringEmbedAvailablePlayerLogos = Field(alias='available_player_logos')

    # Whether the embedded RLE player should display the author's name.
    byline: bool = Field(alias='byline')

    # The chat's iFrame source URL.
    chat_embed_source: typing.Optional[str] = Field(alias='chat_embed_source')

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool = Field(alias='chromecast')

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool = Field(alias='closed_captions')

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color: str = Field(alias='color')

    colors: LiveEventRecurringEmbedColors = Field(alias='colors')

    # The embed code for RLE chat.
    embed_chat: typing.Optional[str] = Field(alias='embed_chat')

    embed_properties: LiveEventRecurringEmbedEmbedProperties = Field(alias='embed_properties')

    # Whether the embedded RLE player should display the event schedule.
    event_schedule: bool = Field(alias='event_schedule')

    # Whether the embedded RLE player should include the fullscreen controls.
    fullscreen_button: bool = Field(alias='fullscreen_button')

    # Whether the Live label should be visible over the player.
    hide_live_label: bool = Field(alias='hide_live_label')

    # Whether the embedded RLE player should hide the viewer counter.
    hide_viewer_count: bool = Field(alias='hide_viewer_count')

    # The fixed HTML code to embed the event's playlist on a website.
    html: typing.Optional[str] = Field(alias='html')

    # Whether the embedded RLE player should include the `like` button.
    like_button: bool = Field(alias='like_button')

    logos: LiveEventRecurringEmbedLogos = Field(alias='logos')

    # Whether the embedded RLE player should loop back to the first video once content is exhausted.
    loop: bool = Field(alias='loop')

    # Whether picture-in-picture is enabled and the button appears in the embeddable player.
    pip: bool = Field(alias='pip')

    # The position of the player's play button.  Option descriptions:  * `0` - The play button has the default position.  * `1` - The play button appears at the bottom of the interface.  * `2` - The play button appears in the center of the interface. 
    play_button_position: Literal["0", "1", "2"] = Field(alias='play_button_position')

    # Whether the embedded RLE player should include the playbar.
    playbar: bool = Field(alias='playbar')

    # Whether the playlist component appears in the embeddable player for this RLE.
    playlist: bool = Field(alias='playlist')

    # Whether the embedded RLE player should display the author's portrait.
    portrait: bool = Field(alias='portrait')

    # The responsive HTML code to embed the event's playlist on a website.
    responsive_html: typing.Optional[str] = Field(alias='responsive_html')

    # Whether the schedule component appears in the embeddable player for this RLE.
    schedule: bool = Field(alias='schedule')

    # Whether the embedded RLE player should display the latest video placeholder.
    show_latest_archived_clip: bool = Field(alias='show_latest_archived_clip')

    # Whether the embedded RLE player should display the schedule timezone.
    show_timezone: bool = Field(alias='show_timezone')

    # Whether the embedded RLE player should use a custom color or the default Vimeo blue.
    use_color: str = Field(alias='use_color')

    # Whether the embedded RLE player should include the volume controls.
    volume: bool = Field(alias='volume')
    class Config:
        arbitrary_types_allowed = True

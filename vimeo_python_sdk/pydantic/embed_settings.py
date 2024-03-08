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

from vimeo_python_sdk.pydantic.email_capture_form import EmailCaptureForm
from vimeo_python_sdk.pydantic.embed_settings_badges import EmbedSettingsBadges
from vimeo_python_sdk.pydantic.embed_settings_buttons import EmbedSettingsButtons
from vimeo_python_sdk.pydantic.embed_settings_cards import EmbedSettingsCards
from vimeo_python_sdk.pydantic.embed_settings_colors import EmbedSettingsColors
from vimeo_python_sdk.pydantic.embed_settings_end_screen import EmbedSettingsEndScreen
from vimeo_python_sdk.pydantic.embed_settings_logos import EmbedSettingsLogos
from vimeo_python_sdk.pydantic.embed_settings_play_button import EmbedSettingsPlayButton
from vimeo_python_sdk.pydantic.embed_settings_title import EmbedSettingsTitle

class EmbedSettings(BaseModel):
    title: EmbedSettingsTitle = Field(alias='title')

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool = Field(alias='airplay')

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: bool = Field(alias='audio_tracks')

    # Whether automatic picture-in-picture is enabled.
    autopip: bool = Field(alias='autopip')

    badges: EmbedSettingsBadges = Field(alias='badges')

    buttons: EmbedSettingsButtons = Field(alias='buttons')

    cards: EmbedSettingsCards = Field(alias='cards')

    # Whether chapters are enabled in the embeddable player.
    chapters: bool = Field(alias='chapters')

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool = Field(alias='chromecast')

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool = Field(alias='closed_captions')

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color: str = Field(alias='color')

    colors: EmbedSettingsColors = Field(alias='colors')

    # The email capture form settings associated with the video.
    email_capture_form: EmailCaptureForm = Field(alias='email_capture_form')

    end_screen: EmbedSettingsEndScreen = Field(alias='end_screen')

    # Whether the embedded player should display the event schedule.
    event_schedule: bool = Field(alias='event_schedule')

    # Whether the video has cards.
    has_cards: bool = Field(alias='has_cards')

    # Whether the video is an interactive video.
    interactive: bool = Field(alias='interactive')

    logos: EmbedSettingsLogos = Field(alias='logos')

    # The type of the video outro.  Option descriptions:  * `beginning` - The outro is a thumbnail.  * `custom` - The outro is custom.  * `email` - The outro is an email form.  * `image` - The outro is an image.  * `link` - The outro is a link.  * `loop` - The outro is a loop.  * `nothing` - There is no outro.  * `share` - The outro is a share button.  * `text` - The outro is text.  * `threevideos` - The outro is three video suggestions.  * `videos` - The outro is video suggestions. 
    outro_type: Literal["beginning", "custom", "email", "image", "link", "loop", "nothing", "share", "text", "threevideos", "videos"] = Field(alias='outro_type')

    # Whether picture-in-picture is enabled and the button appears in the embeddable player.
    pip: bool = Field(alias='pip')

    play_button: EmbedSettingsPlayButton = Field(alias='play_button')

    # Whether the playbar appears in the embeddable player.
    playbar: bool = Field(alias='playbar')

    # Whether the quality selector appears in the embeddable player.
    quality_selector: bool = Field(alias='quality_selector')

    # Whether the embedded player should display the schedule timezone.
    show_timezone: bool = Field(alias='show_timezone')

    # Whether the speed controls appear in the embeddable player.
    speed: bool = Field(alias='speed')

    # Whether the transcript controls appear in the embeddable player.
    transcript: bool = Field(alias='transcript')

    # Whether the volume controls appear in the embeddable player.
    volume: bool = Field(alias='volume')

    # The HTML code for embedding the video on a web page.
    html: typing.Optional[str] = Field(None, alias='html')

    # The URI of the embed preset.
    uri: typing.Optional[str] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True

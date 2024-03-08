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

from vimeo_python_sdk.type.email_capture_form import EmailCaptureForm
from vimeo_python_sdk.type.embed_settings_badges import EmbedSettingsBadges
from vimeo_python_sdk.type.embed_settings_buttons import EmbedSettingsButtons
from vimeo_python_sdk.type.embed_settings_cards import EmbedSettingsCards
from vimeo_python_sdk.type.embed_settings_colors import EmbedSettingsColors
from vimeo_python_sdk.type.embed_settings_end_screen import EmbedSettingsEndScreen
from vimeo_python_sdk.type.embed_settings_logos import EmbedSettingsLogos
from vimeo_python_sdk.type.embed_settings_play_button import EmbedSettingsPlayButton
from vimeo_python_sdk.type.embed_settings_title import EmbedSettingsTitle

class RequiredEmbedSettings(TypedDict):
    title: EmbedSettingsTitle

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: bool

    # Whether automatic picture-in-picture is enabled.
    autopip: bool

    badges: EmbedSettingsBadges

    buttons: EmbedSettingsButtons

    cards: EmbedSettingsCards

    # Whether chapters are enabled in the embeddable player.
    chapters: bool

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color: str

    colors: EmbedSettingsColors

    # The email capture form settings associated with the video.
    email_capture_form: EmailCaptureForm

    end_screen: EmbedSettingsEndScreen

    # Whether the embedded player should display the event schedule.
    event_schedule: bool

    # Whether the video has cards.
    has_cards: bool

    # Whether the video is an interactive video.
    interactive: bool

    logos: EmbedSettingsLogos

    # The type of the video outro.  Option descriptions:  * `beginning` - The outro is a thumbnail.  * `custom` - The outro is custom.  * `email` - The outro is an email form.  * `image` - The outro is an image.  * `link` - The outro is a link.  * `loop` - The outro is a loop.  * `nothing` - There is no outro.  * `share` - The outro is a share button.  * `text` - The outro is text.  * `threevideos` - The outro is three video suggestions.  * `videos` - The outro is video suggestions. 
    outro_type: str

    # Whether picture-in-picture is enabled and the button appears in the embeddable player.
    pip: bool

    play_button: EmbedSettingsPlayButton

    # Whether the playbar appears in the embeddable player.
    playbar: bool

    # Whether the quality selector appears in the embeddable player.
    quality_selector: bool

    # Whether the embedded player should display the schedule timezone.
    show_timezone: bool

    # Whether the speed controls appear in the embeddable player.
    speed: bool

    # Whether the transcript controls appear in the embeddable player.
    transcript: bool

    # Whether the volume controls appear in the embeddable player.
    volume: bool

class OptionalEmbedSettings(TypedDict, total=False):
    # The HTML code for embedding the video on a web page.
    html: str

    # The URI of the embed preset.
    uri: str

class EmbedSettings(RequiredEmbedSettings, OptionalEmbedSettings):
    pass

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

from vimeo_python_sdk.type.preset_settings_buttons import PresetSettingsButtons
from vimeo_python_sdk.type.preset_settings_colors import PresetSettingsColors
from vimeo_python_sdk.type.preset_settings_logos import PresetSettingsLogos
from vimeo_python_sdk.type.preset_settings_outro import PresetSettingsOutro
from vimeo_python_sdk.type.preset_settings_play_button import PresetSettingsPlayButton

class RequiredPresetSettings(TypedDict):
    # How the embeddable player handles the video title.  Option descriptions:  * `hide` - The title is hidden.  * `show` - The title is shown.  * `user` - The title can be toggled to `show` or `hide` by the user. 
    title: str

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: bool

    buttons: PresetSettingsButtons

    # How the embeddable player handles the video owner's information.  Option descriptions:  * `hide` - The owner's information is hidden.  * `show` - The owner's information is shown.  * `user` - The owner's information can be toggled to `show` or `hide` by the user. 
    byline: str

    # Whether chapters are enabled in the embeddable player.
    chapters: bool

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color: str

    colors: PresetSettingsColors

    logos: PresetSettingsLogos

    outro: PresetSettingsOutro

    # Whether picture-in-picture is enabled and the button appears in the embeddable player.
    pip: bool

    play_button: PresetSettingsPlayButton

    # Whether the playbar appears in the embeddable player.
    playbar: bool

    # How the embeddable player handles the video owner's portrait.  Option descriptions:  * `hide` - The owner's portrait is hidden.  * `show` - The owner's portrait is shown.  * `user` - The owner's portrait can be toggled to `show` or `hide` by the user. 
    portrait: str

    # Whether to show the quality selector in the embeddable player.
    quality_selector: bool

    # Whether the speed controls appear in the embeddable player.
    speed: bool

    # Whether the transcript controls appear in the embeddable player.
    transcript: bool

    # Whether the volume controls appear in the embeddable player.
    volume: bool

class OptionalPresetSettings(TypedDict, total=False):
    pass

class PresetSettings(RequiredPresetSettings, OptionalPresetSettings):
    pass

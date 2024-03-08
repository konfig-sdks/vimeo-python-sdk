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

from vimeo_python_sdk.pydantic.preset_settings_buttons import PresetSettingsButtons
from vimeo_python_sdk.pydantic.preset_settings_colors import PresetSettingsColors
from vimeo_python_sdk.pydantic.preset_settings_logos import PresetSettingsLogos
from vimeo_python_sdk.pydantic.preset_settings_outro import PresetSettingsOutro
from vimeo_python_sdk.pydantic.preset_settings_play_button import PresetSettingsPlayButton

class PresetSettings(BaseModel):
    # How the embeddable player handles the video title.  Option descriptions:  * `hide` - The title is hidden.  * `show` - The title is shown.  * `user` - The title can be toggled to `show` or `hide` by the user. 
    title: Literal["hide", "show", "user"] = Field(alias='title')

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool = Field(alias='airplay')

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: bool = Field(alias='audio_tracks')

    buttons: PresetSettingsButtons = Field(alias='buttons')

    # How the embeddable player handles the video owner's information.  Option descriptions:  * `hide` - The owner's information is hidden.  * `show` - The owner's information is shown.  * `user` - The owner's information can be toggled to `show` or `hide` by the user. 
    byline: Literal["hide", "show", "user"] = Field(alias='byline')

    # Whether chapters are enabled in the embeddable player.
    chapters: bool = Field(alias='chapters')

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool = Field(alias='chromecast')

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool = Field(alias='closed_captions')

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color: str = Field(alias='color')

    colors: PresetSettingsColors = Field(alias='colors')

    logos: PresetSettingsLogos = Field(alias='logos')

    outro: PresetSettingsOutro = Field(alias='outro')

    # Whether picture-in-picture is enabled and the button appears in the embeddable player.
    pip: bool = Field(alias='pip')

    play_button: PresetSettingsPlayButton = Field(alias='play_button')

    # Whether the playbar appears in the embeddable player.
    playbar: bool = Field(alias='playbar')

    # How the embeddable player handles the video owner's portrait.  Option descriptions:  * `hide` - The owner's portrait is hidden.  * `show` - The owner's portrait is shown.  * `user` - The owner's portrait can be toggled to `show` or `hide` by the user. 
    portrait: Literal["hide", "show", "user"] = Field(alias='portrait')

    # Whether to show the quality selector in the embeddable player.
    quality_selector: bool = Field(alias='quality_selector')

    # Whether the speed controls appear in the embeddable player.
    speed: bool = Field(alias='speed')

    # Whether the transcript controls appear in the embeddable player.
    transcript: bool = Field(alias='transcript')

    # Whether the volume controls appear in the embeddable player.
    volume: bool = Field(alias='volume')
    class Config:
        arbitrary_types_allowed = True

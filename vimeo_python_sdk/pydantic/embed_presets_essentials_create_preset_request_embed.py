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

from vimeo_python_sdk.pydantic.embed_presets_essentials_create_preset_request_embed_buttons import EmbedPresetsEssentialsCreatePresetRequestEmbedButtons
from vimeo_python_sdk.pydantic.embed_presets_essentials_create_preset_request_embed_colors import EmbedPresetsEssentialsCreatePresetRequestEmbedColors
from vimeo_python_sdk.pydantic.embed_presets_essentials_create_preset_request_embed_logos import EmbedPresetsEssentialsCreatePresetRequestEmbedLogos
from vimeo_python_sdk.pydantic.embed_presets_essentials_create_preset_request_embed_play_button import EmbedPresetsEssentialsCreatePresetRequestEmbedPlayButton
from vimeo_python_sdk.pydantic.embed_presets_essentials_create_preset_request_embed_title import EmbedPresetsEssentialsCreatePresetRequestEmbedTitle

class EmbedPresetsEssentialsCreatePresetRequestEmbed(BaseModel):
    title: typing.Optional[EmbedPresetsEssentialsCreatePresetRequestEmbedTitle] = Field(None, alias='title')

    # Whether AirPlay is enabled in the embeddable player.
    airplay: typing.Optional[bool] = Field(None, alias='airplay')

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: typing.Optional[bool] = Field(None, alias='audio_tracks')

    buttons: typing.Optional[EmbedPresetsEssentialsCreatePresetRequestEmbedButtons] = Field(None, alias='buttons')

    # Whether chapters are enabled in the embeddable player.
    chapters: typing.Optional[bool] = Field(None, alias='chapters')

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: typing.Optional[bool] = Field(None, alias='chromecast')

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: typing.Optional[bool] = Field(None, alias='closed_captions')

    # The main color of the embeddable player.
    color: typing.Optional[str] = Field(None, alias='color')

    colors: typing.Optional[EmbedPresetsEssentialsCreatePresetRequestEmbedColors] = Field(None, alias='colors')

    logos: typing.Optional[EmbedPresetsEssentialsCreatePresetRequestEmbedLogos] = Field(None, alias='logos')

    play_button: typing.Optional[EmbedPresetsEssentialsCreatePresetRequestEmbedPlayButton] = Field(None, alias='play_button')

    # Whether to show the playbar on the embeddable player.
    playbar: typing.Optional[bool] = Field(None, alias='playbar')

    # Whether to show the quality selector in the embeddable player.
    quality_selector: typing.Optional[bool] = Field(None, alias='quality_selector')

    # Whether the transcript controls appear in the embeddable player.
    transcript: typing.Optional[bool] = Field(None, alias='transcript')

    # Whether to show the volume selector on the embeddable player.
    volume: typing.Optional[bool] = Field(None, alias='volume')
    class Config:
        arbitrary_types_allowed = True

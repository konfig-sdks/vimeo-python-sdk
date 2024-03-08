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

from vimeo_python_sdk.type.embed_presets_essentials_create_embed_preset_request_embed_buttons import EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedButtons
from vimeo_python_sdk.type.embed_presets_essentials_create_embed_preset_request_embed_colors import EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedColors
from vimeo_python_sdk.type.embed_presets_essentials_create_embed_preset_request_embed_logos import EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogos
from vimeo_python_sdk.type.embed_presets_essentials_create_embed_preset_request_embed_play_button import EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton
from vimeo_python_sdk.type.embed_presets_essentials_create_embed_preset_request_embed_title import EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedTitle

class RequiredEmbedPresetsEssentialsCreateEmbedPresetRequestEmbed(TypedDict):
    pass

class OptionalEmbedPresetsEssentialsCreateEmbedPresetRequestEmbed(TypedDict, total=False):
    title: EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedTitle

    # Whether AirPlay is enabled in the embeddable player.
    airplay: bool

    # Whether multiple audio tracks can appear in the embeddable player.
    audio_tracks: bool

    buttons: EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedButtons

    # Whether chapters are enabled in the embeddable player.
    chapters: bool

    # Whether the Chromecast button appears in the embeddable player.
    chromecast: bool

    # Whether closed captions are enabled in the embeddable player.
    closed_captions: bool

    # The main color of the embeddable player.
    color: str

    colors: EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedColors

    logos: EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogos

    play_button: EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton

    # Whether to show the playbar on the embeddable player.
    playbar: bool

    # Whether to show the quality selector in the embeddable player.
    quality_selector: bool

    # Whether the transcript controls appear in the embeddable player.
    transcript: bool

    # Whether to show the volume selector on the embeddable player.
    volume: bool

class EmbedPresetsEssentialsCreateEmbedPresetRequestEmbed(RequiredEmbedPresetsEssentialsCreateEmbedPresetRequestEmbed, OptionalEmbedPresetsEssentialsCreateEmbedPresetRequestEmbed):
    pass

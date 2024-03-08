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

from vimeo_python_sdk.type.embed_presets_essentials_create_preset_request_embed import EmbedPresetsEssentialsCreatePresetRequestEmbed

class RequiredEmbedPresetsEssentialsCreatePresetRequest(TypedDict):
    pass

class OptionalEmbedPresetsEssentialsCreatePresetRequest(TypedDict, total=False):
    embed: EmbedPresetsEssentialsCreatePresetRequestEmbed

    # The name of the embed preset.
    name: str

class EmbedPresetsEssentialsCreatePresetRequest(RequiredEmbedPresetsEssentialsCreatePresetRequest, OptionalEmbedPresetsEssentialsCreatePresetRequest):
    pass

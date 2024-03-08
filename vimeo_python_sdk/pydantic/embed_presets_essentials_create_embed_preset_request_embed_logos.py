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

from vimeo_python_sdk.pydantic.embed_presets_essentials_create_embed_preset_request_embed_logos_custom import EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom

class EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogos(BaseModel):
    custom: typing.Optional[EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom] = Field(None, alias='custom')

    # Whether to show the Vimeo logo on the embeddable player.
    vimeo: typing.Optional[bool] = Field(None, alias='vimeo')
    class Config:
        arbitrary_types_allowed = True

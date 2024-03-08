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

from vimeo_python_sdk.type.embed_settings_logos_custom import EmbedSettingsLogosCustom

class RequiredEmbedSettingsLogos(TypedDict):
    custom: EmbedSettingsLogosCustom

    # Whether the Vimeo logo appears in the embeddable player.
    vimeo: bool

class OptionalEmbedSettingsLogos(TypedDict, total=False):
    pass

class EmbedSettingsLogos(RequiredEmbedSettingsLogos, OptionalEmbedSettingsLogos):
    pass

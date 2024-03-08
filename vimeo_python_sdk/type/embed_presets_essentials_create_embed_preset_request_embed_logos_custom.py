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


class RequiredEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom(TypedDict):
    pass

class OptionalEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom(TypedDict, total=False):
    # Whether to show the active custom logo on the embeddable player.
    active: bool

    # The ID of the custom logo that appears on the embeddable player.
    id: typing.Optional[typing.Union[int, float]]

    # The URL that loads when the user clicks the custom logo.
    link: typing.Optional[str]

    # Whether the custom logo is always visible on the embeddable player (`true`) or whether the logo appears and disappears with the rest of the UI (`false`).
    sticky: bool

class EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom(RequiredEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom, OptionalEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedLogosCustom):
    pass

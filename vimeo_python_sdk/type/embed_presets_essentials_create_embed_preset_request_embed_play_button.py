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


class RequiredEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton(TypedDict):
    pass

class OptionalEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton(TypedDict, total=False):
    # The position of the play button within the embeddable player.  Option descriptions:  * `auto` - Use Vimeo's default positioning for the play button.  * `bottom` - The play button is positioned at the bottom of the player, except when in tiny mode.  * `center` - The play button is positioned in the center of the player. 
    position: str

class EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton(RequiredEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton, OptionalEmbedPresetsEssentialsCreateEmbedPresetRequestEmbedPlayButton):
    pass

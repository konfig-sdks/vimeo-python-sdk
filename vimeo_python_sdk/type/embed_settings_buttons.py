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


class RequiredEmbedSettingsButtons(TypedDict):
    # Whether the `embed` button appears in the embeddable player.
    embed: bool

    # Whether the `fullscreen` button appears in the embeddable player.
    fullscreen: bool

    # Whether the `HD` button appears in the embeddable player.
    hd: bool

    # Whether the `like` button appears in the embeddable player.
    like: bool

    # Whether the reaction button appears in the embeddable player.
    reaction: typing.Optional[bool]

    # Whether the `scaling` button appears in the embeddable player.
    scaling: bool

    # Whether the `share` button appears in the embeddable player.
    share: bool

    # Whether the `watch later` button appears in the embeddable player.
    watchlater: bool

class OptionalEmbedSettingsButtons(TypedDict, total=False):
    pass

class EmbedSettingsButtons(RequiredEmbedSettingsButtons, OptionalEmbedSettingsButtons):
    pass

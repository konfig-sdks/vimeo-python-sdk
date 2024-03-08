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


class RequiredEditVideoRequestEmbedButtons(TypedDict):
    pass

class OptionalEditVideoRequestEmbedButtons(TypedDict, total=False):
    # Whether to show the `embed` button on the embeddable player.
    embed: bool

    # Whether to show the `fullscreen` button on the embeddable player.
    fullscreen: bool

    # Whether to show the `HD` button on the embeddable player.
    hd: bool

    # Whether to show the `like` button on the embeddable player.
    like: bool

    # Whether to show the `scaling` button on the embeddable player in fullscreen mode.
    scaling: bool

    # Whether to show the `share` button on the embeddable player.
    share: bool

    # Whether to show the `watch later` button on the embeddable player.
    watchlater: bool

class EditVideoRequestEmbedButtons(RequiredEditVideoRequestEmbedButtons, OptionalEditVideoRequestEmbedButtons):
    pass

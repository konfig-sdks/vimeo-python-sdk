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


class RequiredAlbumEmbed(TypedDict):
    # The responsive HTML code to embed the showcase's playlist on a website. This field appears only when the showcase has embeddable videos.
    html: typing.Optional[str]

class OptionalAlbumEmbed(TypedDict, total=False):
    pass

class AlbumEmbed(RequiredAlbumEmbed, OptionalAlbumEmbed):
    pass

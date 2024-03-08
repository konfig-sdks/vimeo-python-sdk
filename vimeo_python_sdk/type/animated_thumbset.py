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

from vimeo_python_sdk.type.animated_thumbnail import AnimatedThumbnail

class RequiredAnimatedThumbset(TypedDict):
    # The URI of the video from which the sets of animated thumbnails were created.
    clip_uri: str

    # The time in ISO 8601 format when the GIF was created.
    created_on: str

    # An array of all the animated thumbnails in the set.
    sizes: typing.List[AnimatedThumbnail]

    # The availability of the animated thumbnail.  Option descriptions:  * `cancelled` - The animated thumbnail's creation has been cancelled.  * `completed` - The animated thumbnail has been created.  * `failed` - The animated thumbnail's creation has failed.  * `started` - The animated thumbnail's creation has started. 
    status: str

    # The URI of the set of animated thumbnails.
    uri: str

class OptionalAnimatedThumbset(TypedDict, total=False):
    pass

class AnimatedThumbset(RequiredAnimatedThumbset, OptionalAnimatedThumbset):
    pass

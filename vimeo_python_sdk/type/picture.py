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

from vimeo_python_sdk.type.picture_sizes import PictureSizes

class RequiredPicture(TypedDict):
    # Whether the picture is currently active.
    active: bool

    # The base link to the image file, without any parameters.
    base_link: str

    # Whether the picture is Vimeo's default.
    default_picture: bool

    # The resource key string of the picture.
    resource_key: str

    sizes: PictureSizes

    # The type of picture.  Option descriptions:  * `caution` - The picture isn't appropriate for all ages.  * `custom` - The picture is a custom video image.  * `default` - The picture is the default video image. 
    type: str

    # The URI of the picture.
    uri: str

class OptionalPicture(TypedDict, total=False):
    # The upload URL of the picture. This field appears upon the initial creation of a picture resource.
    link: str

class Picture(RequiredPicture, OptionalPicture):
    pass

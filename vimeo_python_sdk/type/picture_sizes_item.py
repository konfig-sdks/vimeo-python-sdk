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


class RequiredPictureSizesItem(TypedDict):
    # The height of the picture.
    height: typing.Optional[typing.Union[int, float]]

    # The direct link to the image file. For information about the format of the image file, see our [Working with Thumbnail Uploads](https://developer.vimeo.com/api/upload/thumbnails#returning-the-link-to-a-thumbnail) guide.
    link: str

    # The width of the picture.
    width: typing.Union[int, float]

class OptionalPictureSizesItem(TypedDict, total=False):
    # The direct link to the image file with a play button overlay. For information about the format of the image file, see our [Working with Thumbnail Uploads](https://developer.vimeo.com/api/upload/thumbnails#returning-the-link-to-a-thumbnail) guide.
    link_with_play_button: str

class PictureSizesItem(RequiredPictureSizesItem, OptionalPictureSizesItem):
    pass

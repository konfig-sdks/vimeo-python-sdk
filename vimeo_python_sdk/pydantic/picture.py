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

from vimeo_python_sdk.pydantic.picture_sizes import PictureSizes

class Picture(BaseModel):
    # Whether the picture is currently active.
    active: bool = Field(alias='active')

    # The base link to the image file, without any parameters.
    base_link: str = Field(alias='base_link')

    # Whether the picture is Vimeo's default.
    default_picture: bool = Field(alias='default_picture')

    # The resource key string of the picture.
    resource_key: str = Field(alias='resource_key')

    sizes: PictureSizes = Field(alias='sizes')

    # The type of picture.  Option descriptions:  * `caution` - The picture isn't appropriate for all ages.  * `custom` - The picture is a custom video image.  * `default` - The picture is the default video image. 
    type: Literal["caution", "custom", "default"] = Field(alias='type')

    # The URI of the picture.
    uri: str = Field(alias='uri')

    # The upload URL of the picture. This field appears upon the initial creation of a picture resource.
    link: typing.Optional[str] = Field(None, alias='link')
    class Config:
        arbitrary_types_allowed = True

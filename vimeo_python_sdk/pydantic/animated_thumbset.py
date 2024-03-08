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

from vimeo_python_sdk.pydantic.animated_thumbnail import AnimatedThumbnail

class AnimatedThumbset(BaseModel):
    # The URI of the video from which the sets of animated thumbnails were created.
    clip_uri: str = Field(alias='clip_uri')

    # The time in ISO 8601 format when the GIF was created.
    created_on: str = Field(alias='created_on')

    # An array of all the animated thumbnails in the set.
    sizes: typing.List[AnimatedThumbnail] = Field(alias='sizes')

    # The availability of the animated thumbnail.  Option descriptions:  * `cancelled` - The animated thumbnail's creation has been cancelled.  * `completed` - The animated thumbnail has been created.  * `failed` - The animated thumbnail's creation has failed.  * `started` - The animated thumbnail's creation has started. 
    status: Literal["cancelled", "completed", "failed", "started"] = Field(alias='status')

    # The URI of the set of animated thumbnails.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

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


class UploadVideoRequestUpload(BaseModel):
    # The upload approach.  Option descriptions:  * `post` - Use the `post` approach.  * `pull` - Use the `pull` approach.  * `tus` - Use the `tus` approach. 
    approach: Literal["post", "pull", "tus"] = Field(alias='approach')

    # The public URL at which the video is hosted. The URL must be valid for at least 24 hours. Use this parameter when **approach** is `pull`.
    link: typing.Optional[str] = Field(None, alias='link')

    # The app's redirect URL. Use this parameter when **approach** is `post`.
    redirect_url: typing.Optional[str] = Field(None, alias='redirect_url')

    # The size in bytes of the video to upload. The maximum value of this field is `268435456000`, which corresponds to 250 GB.
    size: typing.Optional[str] = Field(None, alias='size')
    class Config:
        arbitrary_types_allowed = True

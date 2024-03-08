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


class VideosVersionsAddVideoVersionRequestUpload(BaseModel):
    # The approach by which to upload the version.  Option descriptions:  * `post` - Use the `post` method.  * `pull` - Use the `pull` method.  * `tus` - Use the `tus` method. 
    approach: Literal["post", "pull", "tus"] = Field(alias='approach')

    # The public URL from which to download the version when **upload.approach** is `pull`. This URL must be valid for at least 24 hours.
    link: typing.Optional[str] = Field(None, alias='link')

    # The app's redirect URL when **upload.approach** is `post`.
    redirect_url: typing.Optional[str] = Field(None, alias='redirect_url')

    # The upload size of the version.
    size: typing.Optional[str] = Field(None, alias='size')
    class Config:
        arbitrary_types_allowed = True

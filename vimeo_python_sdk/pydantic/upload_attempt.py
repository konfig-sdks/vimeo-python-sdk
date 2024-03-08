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

from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.video import Video

class UploadAttempt(BaseModel):
    # The ticket identifier string for the upload.
    ticket_id: str = Field(alias='ticket_id')

    # The upload URL.
    upload_link: str = Field(alias='upload_link')

    # The upload URI.
    uri: str = Field(alias='uri')

    # The owner of the uploaded video.
    user: User = Field(alias='user')

    # The video to upload.
    clip: typing.Optional[Video] = Field(None, alias='clip')

    # The HTML upload form.
    form: typing.Optional[str] = Field(None, alias='form')
    class Config:
        arbitrary_types_allowed = True

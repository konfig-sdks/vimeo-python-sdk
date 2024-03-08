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

from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.video import Video

class RequiredUploadAttempt(TypedDict):
    # The ticket identifier string for the upload.
    ticket_id: str

    # The upload URL.
    upload_link: str

    # The upload URI.
    uri: str

    # The owner of the uploaded video.
    user: User

class OptionalUploadAttempt(TypedDict, total=False):
    # The video to upload.
    clip: Video

    # The HTML upload form.
    form: str

class UploadAttempt(RequiredUploadAttempt, OptionalUploadAttempt):
    pass

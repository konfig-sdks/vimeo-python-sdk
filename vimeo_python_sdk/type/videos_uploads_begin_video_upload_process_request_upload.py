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


class RequiredVideosUploadsBeginVideoUploadProcessRequestUpload(TypedDict):
    # The upload approach.  Option descriptions:  * `post` - Use the `post` approach.  * `pull` - Use the `pull` approach.  * `tus` - Use the `tus` approach. 
    approach: str

class OptionalVideosUploadsBeginVideoUploadProcessRequestUpload(TypedDict, total=False):
    # The public URL at which the video is hosted. The URL must be valid for at least 24 hours. Use this parameter when **approach** is `pull`.
    link: str

    # The app's redirect URL. Use this parameter when **approach** is `post`.
    redirect_url: str

    # The size in bytes of the video to upload. The maximum value of this field is `268435456000`, which corresponds to 250 GB.
    size: str

class VideosUploadsBeginVideoUploadProcessRequestUpload(RequiredVideosUploadsBeginVideoUploadProcessRequestUpload, OptionalVideosUploadsBeginVideoUploadProcessRequestUpload):
    pass

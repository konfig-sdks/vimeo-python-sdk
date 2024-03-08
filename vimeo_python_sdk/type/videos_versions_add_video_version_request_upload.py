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


class RequiredVideosVersionsAddVideoVersionRequestUpload(TypedDict):
    # The approach by which to upload the version.  Option descriptions:  * `post` - Use the `post` method.  * `pull` - Use the `pull` method.  * `tus` - Use the `tus` method. 
    approach: str

class OptionalVideosVersionsAddVideoVersionRequestUpload(TypedDict, total=False):
    # The public URL from which to download the version when **upload.approach** is `pull`. This URL must be valid for at least 24 hours.
    link: str

    # The app's redirect URL when **upload.approach** is `post`.
    redirect_url: str

    # The upload size of the version.
    size: str

class VideosVersionsAddVideoVersionRequestUpload(RequiredVideosVersionsAddVideoVersionRequestUpload, OptionalVideosVersionsAddVideoVersionRequestUpload):
    pass

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

from vimeo_python_sdk.type.videos_versions_add_video_version_request_upload import VideosVersionsAddVideoVersionRequestUpload

class RequiredVideosVersionsAddVideoVersionRequest(TypedDict):
    # The name of the version.
    file_name: str

    upload: VideosVersionsAddVideoVersionRequestUpload

class OptionalVideosVersionsAddVideoVersionRequest(TypedDict, total=False):
    pass

class VideosVersionsAddVideoVersionRequest(RequiredVideosVersionsAddVideoVersionRequest, OptionalVideosVersionsAddVideoVersionRequest):
    pass

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

from vimeo_python_sdk.type.api_app import ApiApp
from vimeo_python_sdk.type.play import Play
from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.video_version_metadata import VideoVersionMetadata
from vimeo_python_sdk.type.video_version_transcode import VideoVersionTranscode
from vimeo_python_sdk.type.video_version_upload import VideoVersionUpload

class RequiredVideoVersion(TypedDict):
    # Whether the video version is currently active.
    active: bool

    # The API app associated with the video version.
    app: ApiApp

    # Whether the version can be restored.
    can_restore_create: bool

    # The storyboard ID of the video version.
    create_storyboard_id: str

    # The time in ISO 8601 format when the video version was created.
    created_time: str

    # The download config associated with the version.
    download_config: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The duration in seconds of the video version.
    duration: typing.Optional[typing.Union[int, float]]

    # The file name of the video version.
    filename: str

    # The size in byes of the video version file.
    filesize: typing.Optional[typing.Union[int, float]]

    # Whether the video has interactive capability.
    has_interactive: bool

    metadata: VideoVersionMetadata

    # The time in ISO 8601 format when the video version was last modified.
    modified_time: str

    # Whether the video has unified resolution. If the value of this field is `false`, the video requires transcoding.
    origin_variable_frame_resolution: bool

    transcode: VideoVersionTranscode

    upload: VideoVersionUpload

    # The time in ISO 8601 format when the video version was uploaded.
    upload_date: typing.Optional[str]

    # The version's canonical relative URI.
    uri: str

    # The owner of the video version.
    user: User

class OptionalVideoVersion(TypedDict, total=False):
    # A description of the video version. This description can make use of the full unicode character set. This field appears in the response only when a corresponding value is present.
    description: str

    # The `Play` representation.
    play: Play

class VideoVersion(RequiredVideoVersion, OptionalVideoVersion):
    pass

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

from vimeo_python_sdk.pydantic.api_app import ApiApp
from vimeo_python_sdk.pydantic.play import Play
from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.video_version_metadata import VideoVersionMetadata
from vimeo_python_sdk.pydantic.video_version_transcode import VideoVersionTranscode
from vimeo_python_sdk.pydantic.video_version_upload import VideoVersionUpload

class VideoVersion(BaseModel):
    # Whether the video version is currently active.
    active: bool = Field(alias='active')

    # The API app associated with the video version.
    app: ApiApp = Field(alias='app')

    # Whether the version can be restored.
    can_restore_create: bool = Field(alias='can_restore_create')

    # The storyboard ID of the video version.
    create_storyboard_id: str = Field(alias='create_storyboard_id')

    # The time in ISO 8601 format when the video version was created.
    created_time: str = Field(alias='created_time')

    # The download config associated with the version.
    download_config: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='download_config')

    # The duration in seconds of the video version.
    duration: typing.Optional[typing.Union[int, float]] = Field(alias='duration')

    # The file name of the video version.
    filename: str = Field(alias='filename')

    # The size in byes of the video version file.
    filesize: typing.Optional[typing.Union[int, float]] = Field(alias='filesize')

    # Whether the video has interactive capability.
    has_interactive: bool = Field(alias='has_interactive')

    metadata: VideoVersionMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the video version was last modified.
    modified_time: str = Field(alias='modified_time')

    # Whether the video has unified resolution. If the value of this field is `false`, the video requires transcoding.
    origin_variable_frame_resolution: bool = Field(alias='origin_variable_frame_resolution')

    transcode: VideoVersionTranscode = Field(alias='transcode')

    upload: VideoVersionUpload = Field(alias='upload')

    # The time in ISO 8601 format when the video version was uploaded.
    upload_date: typing.Optional[str] = Field(alias='upload_date')

    # The version's canonical relative URI.
    uri: str = Field(alias='uri')

    # The owner of the video version.
    user: User = Field(alias='user')

    # A description of the video version. This description can make use of the full unicode character set. This field appears in the response only when a corresponding value is present.
    description: typing.Optional[str] = Field(None, alias='description')

    # The `Play` representation.
    play: typing.Optional[Play] = Field(None, alias='play')
    class Config:
        arbitrary_types_allowed = True

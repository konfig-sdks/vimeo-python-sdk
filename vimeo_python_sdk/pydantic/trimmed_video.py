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

from vimeo_python_sdk.pydantic.trimmed_video_metadata import TrimmedVideoMetadata

class TrimmedVideo(BaseModel):
    # The ID of the video. _This field is deprecated._
    clip_id: typing.Union[int, float] = Field(alias='clip_id')

    # The time in ISO 8601 format when the trim was created.
    created_on: str = Field(alias='created_on')

    # The most recent version of the trimmed video. _This field is deprecated._
    created_version_id: str = Field(alias='created_version_id')

    # The end of the trim from the last trim, in seconds.
    end: str = Field(alias='end')

    # Whether the transcoding jobs for the video file have finished. _This field is deprecated._
    is_clip_finished_transcoding: bool = Field(alias='is_clip_finished_transcoding')

    metadata: TrimmedVideoMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the trim policy was last modified.
    modified_on: typing.Optional[str] = Field(alias='modified_on')

    # The video version that is the source of the trimmed video. _This field is deprecated._
    root_version_id: str = Field(alias='root_version_id')

    # The start of the trim from the last trim, in seconds.
    start: str = Field(alias='start')

    # The URI of the player or the trim service. _This field is deprecated._
    uri: str = Field(alias='uri')

    # The quality of the root version video file.
    version_quality: str = Field(alias='version_quality')
    class Config:
        arbitrary_types_allowed = True

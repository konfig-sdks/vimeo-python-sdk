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


class EditingSession(BaseModel):
    # Whether the video has a watermark.
    has_watermark: bool = Field(alias='has_watermark')

    # Whether the video has been edited by Transcript Video Editing.
    is_edited_by_tve: bool = Field(alias='is_edited_by_tve')

    # Whether the current version of the video is at the maximum resolution.
    is_max_resolution: bool = Field(alias='is_max_resolution')

    # Whether the video has licensed music.
    is_music_licensed: bool = Field(alias='is_music_licensed')

    # Whether the video has been rated.
    is_rated: bool = Field(alias='is_rated')

    # The minimum required Vimeo membership for the user to be able to share the video.
    min_tier_for_movie: str = Field(alias='min_tier_for_movie')

    # The result video hash for the created video.
    result_video_hash: str = Field(alias='result_video_hash')

    # The status of the video.  Option descriptions:  * `done` - The video is finished processing.  * `processing` - The video is still being processed. 
    status: Literal["done", "processing"] = Field(alias='status')

    # The ID of the video's editing session.
    vsid: typing.Union[int, float] = Field(alias='vsid')

    # The version's canonical relative URI.
    version_uri: typing.Optional[str] = Field(None, alias='version_uri')
    class Config:
        arbitrary_types_allowed = True

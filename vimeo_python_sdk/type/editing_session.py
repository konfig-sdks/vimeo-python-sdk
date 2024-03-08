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


class RequiredEditingSession(TypedDict):
    # Whether the video has a watermark.
    has_watermark: bool

    # Whether the video has been edited by Transcript Video Editing.
    is_edited_by_tve: bool

    # Whether the current version of the video is at the maximum resolution.
    is_max_resolution: bool

    # Whether the video has licensed music.
    is_music_licensed: bool

    # Whether the video has been rated.
    is_rated: bool

    # The minimum required Vimeo membership for the user to be able to share the video.
    min_tier_for_movie: str

    # The result video hash for the created video.
    result_video_hash: str

    # The status of the video.  Option descriptions:  * `done` - The video is finished processing.  * `processing` - The video is still being processed. 
    status: str

    # The ID of the video's editing session.
    vsid: typing.Union[int, float]

class OptionalEditingSession(TypedDict, total=False):
    # The version's canonical relative URI.
    version_uri: str

class EditingSession(RequiredEditingSession, OptionalEditingSession):
    pass

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

from vimeo_python_sdk.type.segment_line import SegmentLine
from vimeo_python_sdk.type.segment_words import SegmentWords

class RequiredSegment(TypedDict):
    # Whether the segment is autogenerated.
    autogenerated: bool

    # The cue end timestamp in milliseconds from the start of the video.
    cue_end: typing.Union[int, float]

    # The cue start timestamp in milliseconds from the start of the video.
    cue_start: typing.Union[int, float]

    # Whether the segment is enabled.
    enabled: bool

    # The segment identifier.
    id: str

    # The type of caption that the segment originates from.  Option descriptions:  * `captions` - The segment originates from a captions file.  * `subtitles` - The segment originates from a captions and subtitles file. 
    kind: str

    # The language of the segment.
    language: str

    # The line data for the segment.
    lines: typing.List[SegmentLine]

    # The speaker identifier.
    speaker: str

    # The relative URI of the text track that the segment comes from.
    text_track_uri: str

    # The word data for the segment.
    words: typing.List[SegmentWords]

class OptionalSegment(TypedDict, total=False):
    # The canonical relative URI of the segment's video.
    video_uri: str

class Segment(RequiredSegment, OptionalSegment):
    pass
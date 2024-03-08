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


class RequiredVideoTranscript(TypedDict):
    # The video transcript's language. This data requires a bearer token with the `private` scope.
    language: typing.Optional[str]

class OptionalVideoTranscript(TypedDict, total=False):
    # The video transcript's availability status. This data requires a bearer token with the `private` scope.  Option descriptions:  * `completed` - Transcription is completed. The transcript is available.  * `failed` - There was a transcription error. The transcript isn't available.  * `in_progress` - Transcription is currently underway. The transcript isn't available yet.  * `language_not_supported` - We currently don't support transcribing audio for this video's language.  * `no_speech` - Transcription was completed, but there were no words in the audio to transcribe.  * `not_started` - The transcript job hasn't started.  * `unknown` - There isn't a record of this video's transcription job. 
    status: str

class VideoTranscript(RequiredVideoTranscript, OptionalVideoTranscript):
    pass

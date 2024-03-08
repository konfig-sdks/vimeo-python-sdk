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


class VideoTranscript(BaseModel):
    # The video transcript's language. This data requires a bearer token with the `private` scope.
    language: typing.Optional[str] = Field(alias='language')

    # The video transcript's availability status. This data requires a bearer token with the `private` scope.  Option descriptions:  * `completed` - Transcription is completed. The transcript is available.  * `failed` - There was a transcription error. The transcript isn't available.  * `in_progress` - Transcription is currently underway. The transcript isn't available yet.  * `language_not_supported` - We currently don't support transcribing audio for this video's language.  * `no_speech` - Transcription was completed, but there were no words in the audio to transcribe.  * `not_started` - The transcript job hasn't started.  * `unknown` - There isn't a record of this video's transcription job. 
    status: typing.Optional[Literal["completed", "failed", "in_progress", "language_not_supported", "no_speech", "not_started", "unknown"]] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True

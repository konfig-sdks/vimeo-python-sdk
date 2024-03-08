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

from vimeo_python_sdk.pydantic.fragments_metadata import FragmentsMetadata

class Fragments(BaseModel):
    # The time in ISO 8601 format when the fragment was created.
    created_on: str = Field(alias='created_on')

    metadata: FragmentsMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the fragment was last updated.
    modified_on: str = Field(alias='modified_on')

    # The time in milliseconds of the fragment's _inpoint_, or the time from the start of the video that marks the beginning of the fragment.
    timecode: typing.Union[int, float] = Field(alias='timecode')

    # The URI of the video fragment.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

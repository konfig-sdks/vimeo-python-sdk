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

from vimeo_python_sdk.type.fragments_metadata import FragmentsMetadata

class RequiredFragments(TypedDict):
    # The time in ISO 8601 format when the fragment was created.
    created_on: str

    metadata: FragmentsMetadata

    # The time in ISO 8601 format when the fragment was last updated.
    modified_on: str

    # The time in milliseconds of the fragment's _inpoint_, or the time from the start of the video that marks the beginning of the fragment.
    timecode: typing.Union[int, float]

    # The URI of the video fragment.
    uri: str

class OptionalFragments(TypedDict, total=False):
    pass

class Fragments(RequiredFragments, OptionalFragments):
    pass

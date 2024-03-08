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

from vimeo_python_sdk.type.tag_metadata import TagMetadata

class RequiredTag(TypedDict):
    # The normalized canonical tag name.
    canonical: str

    metadata: TagMetadata

    # The tag value.
    name: str

    # The tag's resource key string.
    resource_key: str

    # The canonical relative URI of the tag.
    uri: str

class OptionalTag(TypedDict, total=False):
    pass

class Tag(RequiredTag, OptionalTag):
    pass

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

from vimeo_python_sdk.pydantic.tag_metadata import TagMetadata

class Tag(BaseModel):
    # The normalized canonical tag name.
    canonical: str = Field(alias='canonical')

    metadata: TagMetadata = Field(alias='metadata')

    # The tag value.
    name: str = Field(alias='name')

    # The tag's resource key string.
    resource_key: str = Field(alias='resource_key')

    # The canonical relative URI of the tag.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

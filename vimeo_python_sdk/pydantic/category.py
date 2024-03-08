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

from vimeo_python_sdk.pydantic.category_metadata import CategoryMetadata
from vimeo_python_sdk.pydantic.category_parent import CategoryParent
from vimeo_python_sdk.pydantic.category_subcategories import CategorySubcategories
from vimeo_python_sdk.pydantic.picture import Picture

class Category(BaseModel):
    # Whether the category is deprecated and should not be used for new categorization.
    is_deprecated: bool = Field(alias='is_deprecated')

    # The most recent time in ISO 8601 format when the video was featured.
    last_video_featured_time: str = Field(alias='last_video_featured_time')

    # The URL to access the category in a browser.
    link: str = Field(alias='link')

    metadata: CategoryMetadata = Field(alias='metadata')

    # The display name that identifies the category.
    name: str = Field(alias='name')

    parent: CategoryParent = Field(alias='parent')

    # The active picture for this category. The default shows vertical color bars.
    pictures: Picture = Field(alias='pictures')

    # The resource key of the category.
    resource_key: str = Field(alias='resource_key')

    # Whether the category isn't a subcategory of another category.
    top_level: bool = Field(alias='top_level')

    # The unique identifier to access the category resource.
    uri: str = Field(alias='uri')

    # The active icon for the category.
    icon: typing.Optional[Picture] = Field(None, alias='icon')

    subcategories: typing.Optional[CategorySubcategories] = Field(None, alias='subcategories')
    class Config:
        arbitrary_types_allowed = True

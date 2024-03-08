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

from vimeo_python_sdk.type.category_metadata import CategoryMetadata
from vimeo_python_sdk.type.category_parent import CategoryParent
from vimeo_python_sdk.type.category_subcategories import CategorySubcategories
from vimeo_python_sdk.type.picture import Picture

class RequiredCategory(TypedDict):
    # Whether the category is deprecated and should not be used for new categorization.
    is_deprecated: bool

    # The most recent time in ISO 8601 format when the video was featured.
    last_video_featured_time: str

    # The URL to access the category in a browser.
    link: str

    metadata: CategoryMetadata

    # The display name that identifies the category.
    name: str

    parent: CategoryParent

    # The active picture for this category. The default shows vertical color bars.
    pictures: Picture

    # The resource key of the category.
    resource_key: str

    # Whether the category isn't a subcategory of another category.
    top_level: bool

    # The unique identifier to access the category resource.
    uri: str

class OptionalCategory(TypedDict, total=False):
    # The active icon for the category.
    icon: Picture

    subcategories: CategorySubcategories

class Category(RequiredCategory, OptionalCategory):
    pass

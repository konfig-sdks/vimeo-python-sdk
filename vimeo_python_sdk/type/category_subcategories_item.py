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


class RequiredCategorySubcategoriesItem(TypedDict):
    # The URL to access the subcategory in a browser.
    link: str

    # The display name that identifies the subcategory.
    name: str

    # The unique identifier to access the subcategory. resource.
    uri: str

class OptionalCategorySubcategoriesItem(TypedDict, total=False):
    pass

class CategorySubcategoriesItem(RequiredCategorySubcategoriesItem, OptionalCategorySubcategoriesItem):
    pass

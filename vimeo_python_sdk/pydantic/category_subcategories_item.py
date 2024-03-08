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


class CategorySubcategoriesItem(BaseModel):
    # The URL to access the subcategory in a browser.
    link: str = Field(alias='link')

    # The display name that identifies the subcategory.
    name: str = Field(alias='name')

    # The unique identifier to access the subcategory. resource.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

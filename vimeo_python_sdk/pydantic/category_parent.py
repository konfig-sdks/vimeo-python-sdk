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


class CategoryParent(BaseModel):
    # The URL to access the parent category in a browser.
    link: str = Field(alias='link')

    # The display name that identifies the parent category.
    name: str = Field(alias='name')

    # The unique identifier to access the parent of the category resource.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

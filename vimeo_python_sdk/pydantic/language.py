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


class Language(BaseModel):
    # The standard ISO 639-1 code for the language.
    code: str = Field(alias='code')

    # The name of the language.
    name: str = Field(alias='name')
    class Config:
        arbitrary_types_allowed = True

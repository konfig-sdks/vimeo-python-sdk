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


class AuthError(BaseModel):
    # The name of the error.
    error: str = Field(alias='error')

    # The description of the error.
    error_description: str = Field(alias='error_description')
    class Config:
        arbitrary_types_allowed = True
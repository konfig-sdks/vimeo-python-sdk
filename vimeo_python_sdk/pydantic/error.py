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


class Error(BaseModel):
    # The error message that technical users receive.
    developer_message: str = Field(alias='developer_message')

    # The error message that general users receive.
    error: str = Field(alias='error')

    # The error code.
    error_code: typing.Union[int, float] = Field(alias='error_code')

    # A link to more information about the error.
    link: str = Field(alias='link')
    class Config:
        arbitrary_types_allowed = True

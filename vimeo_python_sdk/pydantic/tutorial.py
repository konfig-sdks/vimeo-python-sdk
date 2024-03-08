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


class Tutorial(BaseModel):
    # The success message.
    message: str = Field(alias='message')

    # The link to the next tutorial.
    next_steps_link: str = Field(alias='next_steps_link')

    # Whether the current access token is authenticated.
    token_is_authenticated: bool = Field(alias='token_is_authenticated')
    class Config:
        arbitrary_types_allowed = True

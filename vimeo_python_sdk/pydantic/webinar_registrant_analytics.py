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


class WebinarRegistrantAnalytics(BaseModel):
    # The percentage of the total webinar that the webinar registrant has attended.
    view_percentage: typing.Union[int, float] = Field(alias='view_percentage')
    class Config:
        arbitrary_types_allowed = True

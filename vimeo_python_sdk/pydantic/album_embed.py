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


class AlbumEmbed(BaseModel):
    # The responsive HTML code to embed the showcase's playlist on a website. This field appears only when the showcase has embeddable videos.
    html: typing.Optional[str] = Field(alias='html')
    class Config:
        arbitrary_types_allowed = True

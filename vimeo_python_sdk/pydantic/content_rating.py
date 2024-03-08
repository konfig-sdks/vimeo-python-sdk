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


class ContentRating(BaseModel):
    # The reason for the content rating.  Option descriptions:  * `advertisement` - The content contains an advertisement.  * `drugs` - The content contains drug or alcohol use.  * `language` - The content contains profanity or sexually suggestive language.  * `nudity` - The content contains nudity.  * `safe` - The content is suitable for all audiences.  * `unrated` - The content hasn't been rated.  * `violence` - The content contains violence or is graphic. 
    code: Literal["advertisement", "drugs", "language", "nudity", "safe", "unrated", "violence"] = Field(alias='code')

    # The name of the content rating.
    name: str = Field(alias='name')

    # The canonical relative URI of the content rating.
    uri: typing.Optional[str] = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

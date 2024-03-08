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


class CreativeCommons(BaseModel):
    # The type of Creative Commons license.  Option descriptions:  * `by` - Attribution.  * `by-nc` - Attribution Non-Commercial.  * `by-nc-nd` - Attribution Non-Commercial No Derivatives.  * `by-nc-sa` - Attribution Non-Commercial Share Alike.  * `by-nd` - Attribution No Derivatives.  * `by-sa` - Attribution Share Alike.  * `cc0` - Public Domain Dedication. 
    code: Literal["by", "by-nc", "by-nc-nd", "by-nc-sa", "by-nd", "by-sa", "cc0"] = Field(alias='code')

    # The description of the Creative Commons license.
    name: str = Field(alias='name')

    # The canonical relative URI of the Creative Commons license.
    uri: typing.Optional[str] = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

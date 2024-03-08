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


class AlbumPrivacy(BaseModel):
    # The access level of the showcase.  Option descriptions:  * `anybody` - Anyone can access the showcase. This privacy setting appears as `Public` on the Vimeo front end.  * `embed_only` - The showcase doesn't appear on Vimeo, but the owner can embed it on other sites.  * `nobody` - No one can access the showacse, including the owner. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the showcase.  * `team` - Only the owner and members of the owner's team can access the showcase.  * `unlisted` - The showcase can't be accessed if the URL omits its unlisted hash. 
    view: Literal["anybody", "embed_only", "nobody", "password", "team", "unlisted"] = Field(alias='view')

    # The showcase's password. This field appears only when **privacy.view** is `password`.
    password: typing.Optional[str] = Field(None, alias='password')
    class Config:
        arbitrary_types_allowed = True

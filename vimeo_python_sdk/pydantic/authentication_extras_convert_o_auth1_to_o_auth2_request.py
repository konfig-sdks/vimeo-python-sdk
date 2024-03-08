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


class AuthenticationExtrasConvertOAuth1ToOAuth2Request(BaseModel):
    # The grant type. The value of this field must be `vimeo_oauth1`.
    grant_type: Literal["vimeo_oauth1"] = Field(alias='grant_type')

    # The OAuth 1 token.
    token: str = Field(alias='token')

    # The OAuth 1 token secret.
    token_secret: str = Field(alias='token_secret')
    class Config:
        arbitrary_types_allowed = True

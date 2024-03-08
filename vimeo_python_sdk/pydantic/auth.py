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

from vimeo_python_sdk.pydantic.api_app import ApiApp
from vimeo_python_sdk.pydantic.user import User

class Auth(BaseModel):
    # The access token string.
    access_token: str = Field(alias='access_token')

    # The API application associated with the token.
    app: ApiApp = Field(alias='app')

    # The scope or scopes that the token supports.
    scope: str = Field(alias='scope')

    # The token type.  Option descriptions:  * `bearer` - The token is of the `bearer` type. 
    token_type: Literal["bearer"] = Field(alias='token_type')

    # The token's expiration date.
    expires_on: typing.Optional[str] = Field(None, alias='expires_on')

    # The refresh token string. The Vimeo API doesn't currently support refresh tokens, but we plan to add this support in the future.
    refresh_token: typing.Optional[str] = Field(None, alias='refresh_token')

    # The user associated with the token.
    user: typing.Optional[User] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True

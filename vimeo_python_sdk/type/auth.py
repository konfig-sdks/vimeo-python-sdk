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

from vimeo_python_sdk.type.api_app import ApiApp
from vimeo_python_sdk.type.user import User

class RequiredAuth(TypedDict):
    # The access token string.
    access_token: str

    # The API application associated with the token.
    app: ApiApp

    # The scope or scopes that the token supports.
    scope: str

    # The token type.  Option descriptions:  * `bearer` - The token is of the `bearer` type. 
    token_type: str

class OptionalAuth(TypedDict, total=False):
    # The token's expiration date.
    expires_on: str

    # The refresh token string. The Vimeo API doesn't currently support refresh tokens, but we plan to add this support in the future.
    refresh_token: str

    # The user associated with the token.
    user: User

class Auth(RequiredAuth, OptionalAuth):
    pass

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


class RequiredAuthenticationExtrasConvertOAuth1ToOAuth2Request(TypedDict):
    # The grant type. The value of this field must be `vimeo_oauth1`.
    grant_type: str

    # The OAuth 1 token.
    token: str

    # The OAuth 1 token secret.
    token_secret: str

class OptionalAuthenticationExtrasConvertOAuth1ToOAuth2Request(TypedDict, total=False):
    pass

class AuthenticationExtrasConvertOAuth1ToOAuth2Request(RequiredAuthenticationExtrasConvertOAuth1ToOAuth2Request, OptionalAuthenticationExtrasConvertOAuth1ToOAuth2Request):
    pass

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


class RequiredAuthenticationExtrasExchangeOAuthCodeExchangeRequest(TypedDict):
    # The authorization code received from the authorization server.
    code: str

    # The grant type. The value of this field must be `authorization_code`.
    grant_type: str

    # The redirect URI. The value of this field must match the URI from `/oauth/authorize`.
    redirect_uri: str

class OptionalAuthenticationExtrasExchangeOAuthCodeExchangeRequest(TypedDict, total=False):
    pass

class AuthenticationExtrasExchangeOAuthCodeExchangeRequest(RequiredAuthenticationExtrasExchangeOAuthCodeExchangeRequest, OptionalAuthenticationExtrasExchangeOAuthCodeExchangeRequest):
    pass

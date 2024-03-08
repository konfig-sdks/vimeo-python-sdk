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


class AuthenticationExtrasExchangeOAuthCodeExchangeRequest(BaseModel):
    # The authorization code received from the authorization server.
    code: str = Field(alias='code')

    # The grant type. The value of this field must be `authorization_code`.
    grant_type: Literal["authorization_code"] = Field(alias='grant_type')

    # The redirect URI. The value of this field must match the URI from `/oauth/authorize`.
    redirect_uri: str = Field(alias='redirect_uri')
    class Config:
        arbitrary_types_allowed = True

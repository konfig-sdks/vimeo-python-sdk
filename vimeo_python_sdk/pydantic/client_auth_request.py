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


class ClientAuthRequest(BaseModel):
    # The grant type. The value of this field must be `client_credentials`.
    grant_type: Literal["client_credentials"] = Field(alias='grant_type')

    # A space-separated list of the authentication scopes to access. The default is `public`.
    scope: str = Field(alias='scope')
    class Config:
        arbitrary_types_allowed = True

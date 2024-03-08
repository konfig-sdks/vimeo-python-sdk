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


class RequiredClientAuthRequest(TypedDict):
    # The grant type. The value of this field must be `client_credentials`.
    grant_type: str

    # A space-separated list of the authentication scopes to access. The default is `public`.
    scope: str

class OptionalClientAuthRequest(TypedDict, total=False):
    pass

class ClientAuthRequest(RequiredClientAuthRequest, OptionalClientAuthRequest):
    pass

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


class RequiredError(TypedDict):
    # The error message that technical users receive.
    developer_message: str

    # The error message that general users receive.
    error: str

    # The error code.
    error_code: typing.Union[int, float]

    # A link to more information about the error.
    link: str

class OptionalError(TypedDict, total=False):
    pass

class Error(RequiredError, OptionalError):
    pass

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


class RequiredTutorial(TypedDict):
    # The success message.
    message: str

    # The link to the next tutorial.
    next_steps_link: str

    # Whether the current access token is authenticated.
    token_is_authenticated: bool

class OptionalTutorial(TypedDict, total=False):
    pass

class Tutorial(RequiredTutorial, OptionalTutorial):
    pass

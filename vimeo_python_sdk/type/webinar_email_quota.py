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


class RequiredWebinarEmailQuota(TypedDict):
    # The maximum number of webinar emails that the user can send.
    capping: typing.Union[int, float]

    # The current number of webinar emails that the user has sent.
    total: typing.Union[int, float]

class OptionalWebinarEmailQuota(TypedDict, total=False):
    pass

class WebinarEmailQuota(RequiredWebinarEmailQuota, OptionalWebinarEmailQuota):
    pass

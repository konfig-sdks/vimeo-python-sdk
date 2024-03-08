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


class RequiredWebinarRegistrantAnalytics(TypedDict):
    # The percentage of the total webinar that the webinar registrant has attended.
    view_percentage: typing.Union[int, float]

class OptionalWebinarRegistrantAnalytics(TypedDict, total=False):
    pass

class WebinarRegistrantAnalytics(RequiredWebinarRegistrantAnalytics, OptionalWebinarRegistrantAnalytics):
    pass

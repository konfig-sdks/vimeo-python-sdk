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

from vimeo_python_sdk.type.webinar_event import WebinarEvent

class RequiredWebinarEvents(TypedDict):
    # The details of the first page of webinar events associated with the webinar.
    data: typing.List[WebinarEvent]

    # The total number of webinar events associated with the webinar.
    total: typing.Union[int, float]

class OptionalWebinarEvents(TypedDict, total=False):
    pass

class WebinarEvents(RequiredWebinarEvents, OptionalWebinarEvents):
    pass

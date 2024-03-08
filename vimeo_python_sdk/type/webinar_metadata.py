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


class RequiredWebinarMetadata(TypedDict):
    # A list of resource URIs related to the webinar.
    connections: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # A list of resource URIs related to the event.
    interactions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalWebinarMetadata(TypedDict, total=False):
    pass

class WebinarMetadata(RequiredWebinarMetadata, OptionalWebinarMetadata):
    pass

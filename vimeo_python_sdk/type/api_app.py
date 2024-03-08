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


class RequiredApiApp(TypedDict):
    # The app's capabilities list.
    capabilities: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The name of the API app.
    name: str

    # The canonical URI of the API app.
    uri: str

class OptionalApiApp(TypedDict, total=False):
    pass

class ApiApp(RequiredApiApp, OptionalApiApp):
    pass

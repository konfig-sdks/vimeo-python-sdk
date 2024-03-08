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


class RequiredEditVodRequestPreorder(TypedDict):
    pass

class OptionalEditVodRequestPreorder(TypedDict, total=False):
    # Whether to enable preorders on the On Demand page.
    active: bool

    # The time in ISO 8601 format when the On Demand page will be published. This parameter is required when **preorder.active** is `true`.
    publish_time: str

class EditVodRequestPreorder(RequiredEditVodRequestPreorder, OptionalEditVodRequestPreorder):
    pass

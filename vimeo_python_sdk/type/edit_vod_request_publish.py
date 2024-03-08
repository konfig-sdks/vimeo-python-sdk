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


class RequiredEditVodRequestPublish(TypedDict):
    pass

class OptionalEditVodRequestPublish(TypedDict, total=False):
    # Whether to publish the On Demand page.
    active: bool

class EditVodRequestPublish(RequiredEditVodRequestPublish, OptionalEditVodRequestPublish):
    pass

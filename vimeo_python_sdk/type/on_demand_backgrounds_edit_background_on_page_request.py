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


class RequiredOnDemandBackgroundsEditBackgroundOnPageRequest(TypedDict):
    pass

class OptionalOnDemandBackgroundsEditBackgroundOnPageRequest(TypedDict, total=False):
    # Whether this background image is the one that appears on the On Demand page.
    active: bool

class OnDemandBackgroundsEditBackgroundOnPageRequest(RequiredOnDemandBackgroundsEditBackgroundOnPageRequest, OptionalOnDemandBackgroundsEditBackgroundOnPageRequest):
    pass

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


class RequiredEditPictureRequest(TypedDict):
    pass

class OptionalEditPictureRequest(TypedDict, total=False):
    # Whether the picture is the authenticated user's active portrait.
    active: bool

class EditPictureRequest(RequiredEditPictureRequest, OptionalEditPictureRequest):
    pass

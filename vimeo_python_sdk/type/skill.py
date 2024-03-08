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


class RequiredSkill(TypedDict):
    # The skill's display name.
    name: str

    # The skill's canonical relative URI.
    uri: str

class OptionalSkill(TypedDict, total=False):
    pass

class Skill(RequiredSkill, OptionalSkill):
    pass

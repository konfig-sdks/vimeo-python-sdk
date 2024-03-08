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


class RequiredDomain(TypedDict):
    # Whether to permit HD embeds on this domain.
    allow_hd: bool

    # The domain name.
    domain: str

    # The URI of the domain.
    uri: str

class OptionalDomain(TypedDict, total=False):
    pass

class Domain(RequiredDomain, OptionalDomain):
    pass

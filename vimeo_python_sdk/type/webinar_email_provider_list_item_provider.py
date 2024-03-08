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


class RequiredWebinarEmailProviderListItemProvider(TypedDict):
    # The dark icon of the connected provider.
    dark_icon: str

    # The standard icon of the connected provider.
    icon: str

    # The ID of the connected provider.
    id: str

    # The name of the connected provider.
    name: str

class OptionalWebinarEmailProviderListItemProvider(TypedDict, total=False):
    pass

class WebinarEmailProviderListItemProvider(RequiredWebinarEmailProviderListItemProvider, OptionalWebinarEmailProviderListItemProvider):
    pass

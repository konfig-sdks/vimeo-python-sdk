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

from vimeo_python_sdk.type.endpoint_methods import EndpointMethods

class RequiredEndpoint(TypedDict):
    methods: EndpointMethods

    # The path section of the URL, which, when appended to the API host `https:///api.vimeo.com`, builds a full API endpoint.
    path: str

class OptionalEndpoint(TypedDict, total=False):
    pass

class Endpoint(RequiredEndpoint, OptionalEndpoint):
    pass

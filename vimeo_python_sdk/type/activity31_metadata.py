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

from vimeo_python_sdk.type.activity31_metadata_connections import Activity31MetadataConnections

class RequiredActivity31Metadata(TypedDict):
    connections: Activity31MetadataConnections

class OptionalActivity31Metadata(TypedDict, total=False):
    pass

class Activity31Metadata(RequiredActivity31Metadata, OptionalActivity31Metadata):
    pass

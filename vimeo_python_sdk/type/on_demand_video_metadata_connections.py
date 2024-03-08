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

from vimeo_python_sdk.type.on_demand_video_metadata_connections_season import OnDemandVideoMetadataConnectionsSeason

class RequiredOnDemandVideoMetadataConnections(TypedDict):
    season: OnDemandVideoMetadataConnectionsSeason

class OptionalOnDemandVideoMetadataConnections(TypedDict, total=False):
    pass

class OnDemandVideoMetadataConnections(RequiredOnDemandVideoMetadataConnections, OptionalOnDemandVideoMetadataConnections):
    pass

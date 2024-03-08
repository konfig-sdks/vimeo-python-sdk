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

from vimeo_python_sdk.type.analytics_metadata_connections_video_options import AnalyticsMetadataConnectionsVideoOptions

class RequiredAnalyticsMetadataConnectionsVideo(TypedDict):
    # The title of the associated video.
    title: str

    # The duration of the associated video.
    duration: typing.Union[int, float]

    options: AnalyticsMetadataConnectionsVideoOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalAnalyticsMetadataConnectionsVideo(TypedDict, total=False):
    pass

class AnalyticsMetadataConnectionsVideo(RequiredAnalyticsMetadataConnectionsVideo, OptionalAnalyticsMetadataConnectionsVideo):
    pass

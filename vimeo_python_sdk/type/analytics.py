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

from vimeo_python_sdk.type.analytics_country import AnalyticsCountry
from vimeo_python_sdk.type.analytics_metadata import AnalyticsMetadata

class RequiredAnalytics(TypedDict):
    # The average percent watched in seconds of the corresponding Vimeo content.
    average_percent_watched: typing.Union[int, float]

    # The average time watched in seconds of the corresponding Vimeo content.
    average_time_watched: typing.Union[int, float]

    country: AnalyticsCountry

    # The number of downloads of the corresponding Vimeo content.
    downloads: typing.Union[int, float]

    # The domain name of the website.
    embed_domain: str

    # The end time of the time interval in ISO 8601 format.
    end_date: str

    # The number of finishes of the corresponding Vimeo content.
    finishes: typing.Union[int, float]

    # The number of impressions of the corresponding Vimeo content.
    impressions: typing.Union[int, float]

    metadata: AnalyticsMetadata

    # The start time of the time interval in ISO 8601 format.
    start_date: str

    # The total time watched in seconds of the corresponding Vimeo content.
    total_time_watched: typing.Union[int, float]

    # The number of unique impressions of the corresponding Vimeo content.
    unique_impressions: typing.Union[int, float]

    # The number of unique viewers of the corresponding Vimeo content.
    unique_viewers: typing.Union[int, float]

    # The number of views of the corresponding Vimeo content.
    views: typing.Union[int, float]

class OptionalAnalytics(TypedDict, total=False):
    pass

class Analytics(RequiredAnalytics, OptionalAnalytics):
    pass

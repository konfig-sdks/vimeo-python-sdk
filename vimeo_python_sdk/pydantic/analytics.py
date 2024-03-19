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
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.analytics_country import AnalyticsCountry
from vimeo_python_sdk.pydantic.analytics_metadata import AnalyticsMetadata

class Analytics(BaseModel):
    # The average percent watched in seconds of the corresponding Vimeo content.
    average_percent_watched: typing.Union[int, float] = Field(alias='average_percent_watched')

    # The average time watched in seconds of the corresponding Vimeo content.
    average_time_watched: typing.Union[int, float] = Field(alias='average_time_watched')

    country: AnalyticsCountry = Field(alias='country')

    # The type of device.
    device_type: str = Field(alias='device_type')

    # The number of downloads of the corresponding Vimeo content.
    downloads: typing.Union[int, float] = Field(alias='downloads')

    # The domain name of the website.
    embed_domain: str = Field(alias='embed_domain')

    # The end time of the time interval in ISO 8601 format.
    end_date: str = Field(alias='end_date')

    # The number of finishes of the corresponding Vimeo content.
    finishes: typing.Union[int, float] = Field(alias='finishes')

    # The number of impressions of the corresponding Vimeo content.
    impressions: typing.Union[int, float] = Field(alias='impressions')

    metadata: AnalyticsMetadata = Field(alias='metadata')

    # The start time of the time interval in ISO 8601 format.
    start_date: str = Field(alias='start_date')

    # The total time watched in seconds of the corresponding Vimeo content.
    total_time_watched: typing.Union[int, float] = Field(alias='total_time_watched')

    # The number of unique impressions of the corresponding Vimeo content.
    unique_impressions: typing.Union[int, float] = Field(alias='unique_impressions')

    # The number of unique viewers of the corresponding Vimeo content.
    unique_viewers: typing.Union[int, float] = Field(alias='unique_viewers')

    # The number of views of the corresponding Vimeo content.
    views: typing.Union[int, float] = Field(alias='views')
    class Config:
        arbitrary_types_allowed = True

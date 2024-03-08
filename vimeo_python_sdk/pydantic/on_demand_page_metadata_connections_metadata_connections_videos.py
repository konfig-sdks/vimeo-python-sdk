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

from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_videos_options import OnDemandPageMetadataConnectionsMetadataConnectionsVideosOptions

class OnDemandPageMetadataConnectionsMetadataConnectionsVideos(BaseModel):
    # The total number of extra videos on the On Demand page.
    extra_total: typing.Union[int, float] = Field(alias='extra_total')

    # The total number of main videos on the On Demand page.
    main_total: typing.Union[int, float] = Field(alias='main_total')

    options: OnDemandPageMetadataConnectionsMetadataConnectionsVideosOptions = Field(alias='options')

    # The total number of videos on this connection.
    total: typing.Union[int, float] = Field(alias='total')

    # The API URI that resolves to the connection data.
    uri: str = Field(alias='uri')

    # The total number of viewable videos on the On Demand page.
    viewable_total: typing.Union[int, float] = Field(alias='viewable_total')
    class Config:
        arbitrary_types_allowed = True

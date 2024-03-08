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

from vimeo_python_sdk.pydantic.video_metadata_connections_pictures_options import VideoMetadataConnectionsPicturesOptions

class VideoMetadataConnectionsPictures(BaseModel):
    options: VideoMetadataConnectionsPicturesOptions = Field(alias='options')

    # Total number of thumbnails on this connection.
    total: typing.Union[int, float] = Field(alias='total')

    # The API URI that resolves to the connection data.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
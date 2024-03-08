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

from vimeo_python_sdk.pydantic.video_metadata_interactions_edit_privacy_properties_item_options import VideoMetadataInteractionsEditPrivacyPropertiesItemOptions

class VideoMetadataInteractionsEditPrivacyPropertiesItem(BaseModel):
    # The name of the property to be sent.
    name: str = Field(alias='name')

    options: VideoMetadataInteractionsEditPrivacyPropertiesItemOptions = Field(alias='options')

    # Whether the field must be sent to achieve the desired action.
    required: bool = Field(alias='required')
    class Config:
        arbitrary_types_allowed = True

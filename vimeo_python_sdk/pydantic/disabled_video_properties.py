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

from vimeo_python_sdk.pydantic.disabled_video_properties_add_to_collection import DisabledVideoPropertiesAddToCollection
from vimeo_python_sdk.pydantic.disabled_video_properties_download import DisabledVideoPropertiesDownload
from vimeo_python_sdk.pydantic.disabled_video_properties_duplicate import DisabledVideoPropertiesDuplicate
from vimeo_python_sdk.pydantic.disabled_video_properties_edit_privacy import DisabledVideoPropertiesEditPrivacy
from vimeo_python_sdk.pydantic.disabled_video_properties_embed import DisabledVideoPropertiesEmbed
from vimeo_python_sdk.pydantic.disabled_video_properties_embed_presets import DisabledVideoPropertiesEmbedPresets

class DisabledVideoProperties(BaseModel):
    add_to_collection: DisabledVideoPropertiesAddToCollection = Field(alias='add_to_collection')

    download: DisabledVideoPropertiesDownload = Field(alias='download')

    duplicate: DisabledVideoPropertiesDuplicate = Field(alias='duplicate')

    edit_privacy: DisabledVideoPropertiesEditPrivacy = Field(alias='edit_privacy')

    embed: DisabledVideoPropertiesEmbed = Field(alias='embed')

    embed_presets: DisabledVideoPropertiesEmbedPresets = Field(alias='embed_presets')
    class Config:
        arbitrary_types_allowed = True

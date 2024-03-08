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

from vimeo_python_sdk.pydantic.project_metadata_interactions_add_subfolder_options import ProjectMetadataInteractionsAddSubfolderOptions
from vimeo_python_sdk.pydantic.project_metadata_interactions_add_subfolder_properties import ProjectMetadataInteractionsAddSubfolderProperties

class ProjectMetadataInteractionsAddSubfolder(BaseModel):
    # Whether the folder can contain a subfolder.
    can_add_subfolders: bool = Field(alias='can_add_subfolders')

    # Whether the user has reached the maximum subfolder depth.
    subfolder_depth_limit_reached: bool = Field(alias='subfolder_depth_limit_reached')

    # The subfolder content type.
    content_type: typing.Optional[str] = Field(None, alias='content_type')

    options: typing.Optional[ProjectMetadataInteractionsAddSubfolderOptions] = Field(None, alias='options')

    properties: typing.Optional[ProjectMetadataInteractionsAddSubfolderProperties] = Field(None, alias='properties')

    # The API URI that resolves to the connection data.
    uri: typing.Optional[str] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True

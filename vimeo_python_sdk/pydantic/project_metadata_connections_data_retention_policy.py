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

from vimeo_python_sdk.pydantic.project_metadata_connections_data_retention_policy_options import ProjectMetadataConnectionsDataRetentionPolicyOptions

class ProjectMetadataConnectionsDataRetentionPolicy(BaseModel):
    # The title of the data retention policy. This data requires a bearer token with the `private` scope.
    title: str = Field(alias='title')

    options: ProjectMetadataConnectionsDataRetentionPolicyOptions = Field(alias='options')

    # The URI of the data retention policy. This data requires a bearer token with the `private` scope.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

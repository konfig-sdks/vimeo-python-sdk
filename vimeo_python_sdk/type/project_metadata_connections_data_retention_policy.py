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

from vimeo_python_sdk.type.project_metadata_connections_data_retention_policy_options import ProjectMetadataConnectionsDataRetentionPolicyOptions

class RequiredProjectMetadataConnectionsDataRetentionPolicy(TypedDict):
    # The title of the data retention policy. This data requires a bearer token with the `private` scope.
    title: str

    options: ProjectMetadataConnectionsDataRetentionPolicyOptions

    # The URI of the data retention policy. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalProjectMetadataConnectionsDataRetentionPolicy(TypedDict, total=False):
    pass

class ProjectMetadataConnectionsDataRetentionPolicy(RequiredProjectMetadataConnectionsDataRetentionPolicy, OptionalProjectMetadataConnectionsDataRetentionPolicy):
    pass

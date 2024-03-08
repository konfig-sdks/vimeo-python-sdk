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

from vimeo_python_sdk.type.project_metadata_connections_user_folder_access_grants_folder_permission_policies import ProjectMetadataConnectionsUserFolderAccessGrantsFolderPermissionPolicies
from vimeo_python_sdk.type.project_metadata_connections_user_folder_access_grants_options import ProjectMetadataConnectionsUserFolderAccessGrantsOptions

class RequiredProjectMetadataConnectionsUserFolderAccessGrants(TypedDict):
    folder_permission_policies: ProjectMetadataConnectionsUserFolderAccessGrantsFolderPermissionPolicies

    options: ProjectMetadataConnectionsUserFolderAccessGrantsOptions

    # The total number of user folder access grants on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalProjectMetadataConnectionsUserFolderAccessGrants(TypedDict, total=False):
    pass

class ProjectMetadataConnectionsUserFolderAccessGrants(RequiredProjectMetadataConnectionsUserFolderAccessGrants, OptionalProjectMetadataConnectionsUserFolderAccessGrants):
    pass

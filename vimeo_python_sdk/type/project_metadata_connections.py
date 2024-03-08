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

from vimeo_python_sdk.type.project_metadata_connections_ancestor_path import ProjectMetadataConnectionsAncestorPath
from vimeo_python_sdk.type.project_metadata_connections_data_retention import ProjectMetadataConnectionsDataRetention
from vimeo_python_sdk.type.project_metadata_connections_folders import ProjectMetadataConnectionsFolders
from vimeo_python_sdk.type.project_metadata_connections_group_folder_grants import ProjectMetadataConnectionsGroupFolderGrants
from vimeo_python_sdk.type.project_metadata_connections_items import ProjectMetadataConnectionsItems
from vimeo_python_sdk.type.project_metadata_connections_parent_folder import ProjectMetadataConnectionsParentFolder
from vimeo_python_sdk.type.project_metadata_connections_personal_team_folder_owner import ProjectMetadataConnectionsPersonalTeamFolderOwner
from vimeo_python_sdk.type.project_metadata_connections_resource_creator_team_user import ProjectMetadataConnectionsResourceCreatorTeamUser
from vimeo_python_sdk.type.project_metadata_connections_team_permissions import ProjectMetadataConnectionsTeamPermissions
from vimeo_python_sdk.type.project_metadata_connections_user_folder_access_grants import ProjectMetadataConnectionsUserFolderAccessGrants
from vimeo_python_sdk.type.project_metadata_connections_videos import ProjectMetadataConnectionsVideos

class RequiredProjectMetadataConnections(TypedDict):
    ancestor_path: ProjectMetadataConnectionsAncestorPath

    data_retention: ProjectMetadataConnectionsDataRetention

    folders: ProjectMetadataConnectionsFolders

    group_folder_grants: ProjectMetadataConnectionsGroupFolderGrants

    items: ProjectMetadataConnectionsItems

    parent_folder: ProjectMetadataConnectionsParentFolder

    personal_team_folder_owner: ProjectMetadataConnectionsPersonalTeamFolderOwner

    resource_creator_team_user: ProjectMetadataConnectionsResourceCreatorTeamUser

    team_permissions: ProjectMetadataConnectionsTeamPermissions

    user_folder_access_grants: ProjectMetadataConnectionsUserFolderAccessGrants

    videos: ProjectMetadataConnectionsVideos

class OptionalProjectMetadataConnections(TypedDict, total=False):
    pass

class ProjectMetadataConnections(RequiredProjectMetadataConnections, OptionalProjectMetadataConnections):
    pass

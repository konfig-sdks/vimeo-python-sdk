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

from vimeo_python_sdk.pydantic.project_metadata_connections_ancestor_path import ProjectMetadataConnectionsAncestorPath
from vimeo_python_sdk.pydantic.project_metadata_connections_data_retention import ProjectMetadataConnectionsDataRetention
from vimeo_python_sdk.pydantic.project_metadata_connections_folders import ProjectMetadataConnectionsFolders
from vimeo_python_sdk.pydantic.project_metadata_connections_group_folder_grants import ProjectMetadataConnectionsGroupFolderGrants
from vimeo_python_sdk.pydantic.project_metadata_connections_items import ProjectMetadataConnectionsItems
from vimeo_python_sdk.pydantic.project_metadata_connections_parent_folder import ProjectMetadataConnectionsParentFolder
from vimeo_python_sdk.pydantic.project_metadata_connections_personal_team_folder_owner import ProjectMetadataConnectionsPersonalTeamFolderOwner
from vimeo_python_sdk.pydantic.project_metadata_connections_resource_creator_team_user import ProjectMetadataConnectionsResourceCreatorTeamUser
from vimeo_python_sdk.pydantic.project_metadata_connections_team_permissions import ProjectMetadataConnectionsTeamPermissions
from vimeo_python_sdk.pydantic.project_metadata_connections_user_folder_access_grants import ProjectMetadataConnectionsUserFolderAccessGrants
from vimeo_python_sdk.pydantic.project_metadata_connections_videos import ProjectMetadataConnectionsVideos

class ProjectMetadataConnections(BaseModel):
    ancestor_path: ProjectMetadataConnectionsAncestorPath = Field(alias='ancestor_path')

    data_retention: ProjectMetadataConnectionsDataRetention = Field(alias='data_retention')

    folders: ProjectMetadataConnectionsFolders = Field(alias='folders')

    group_folder_grants: ProjectMetadataConnectionsGroupFolderGrants = Field(alias='group_folder_grants')

    items: ProjectMetadataConnectionsItems = Field(alias='items')

    parent_folder: ProjectMetadataConnectionsParentFolder = Field(alias='parent_folder')

    personal_team_folder_owner: ProjectMetadataConnectionsPersonalTeamFolderOwner = Field(alias='personal_team_folder_owner')

    resource_creator_team_user: ProjectMetadataConnectionsResourceCreatorTeamUser = Field(alias='resource_creator_team_user')

    team_permissions: ProjectMetadataConnectionsTeamPermissions = Field(alias='team_permissions')

    user_folder_access_grants: ProjectMetadataConnectionsUserFolderAccessGrants = Field(alias='user_folder_access_grants')

    videos: ProjectMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True

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

from vimeo_python_sdk.pydantic.project_metadata_interactions_add_subfolder import ProjectMetadataInteractionsAddSubfolder
from vimeo_python_sdk.pydantic.project_metadata_interactions_delete import ProjectMetadataInteractionsDelete
from vimeo_python_sdk.pydantic.project_metadata_interactions_delete_video import ProjectMetadataInteractionsDeleteVideo
from vimeo_python_sdk.pydantic.project_metadata_interactions_edit import ProjectMetadataInteractionsEdit
from vimeo_python_sdk.pydantic.project_metadata_interactions_edit_settings import ProjectMetadataInteractionsEditSettings
from vimeo_python_sdk.pydantic.project_metadata_interactions_invite import ProjectMetadataInteractionsInvite
from vimeo_python_sdk.pydantic.project_metadata_interactions_move_video import ProjectMetadataInteractionsMoveVideo
from vimeo_python_sdk.pydantic.project_metadata_interactions_upload_video import ProjectMetadataInteractionsUploadVideo
from vimeo_python_sdk.pydantic.project_metadata_interactions_view import ProjectMetadataInteractionsView

class ProjectMetadataInteractions(BaseModel):
    add_subfolder: ProjectMetadataInteractionsAddSubfolder = Field(alias='add_subfolder')

    delete: ProjectMetadataInteractionsDelete = Field(alias='delete')

    delete_video: ProjectMetadataInteractionsDeleteVideo = Field(alias='delete_video')

    edit: ProjectMetadataInteractionsEdit = Field(alias='edit')

    edit_settings: ProjectMetadataInteractionsEditSettings = Field(alias='edit_settings')

    invite: ProjectMetadataInteractionsInvite = Field(alias='invite')

    move_video: ProjectMetadataInteractionsMoveVideo = Field(alias='move_video')

    upload_video: ProjectMetadataInteractionsUploadVideo = Field(alias='upload_video')

    view: ProjectMetadataInteractionsView = Field(alias='view')
    class Config:
        arbitrary_types_allowed = True

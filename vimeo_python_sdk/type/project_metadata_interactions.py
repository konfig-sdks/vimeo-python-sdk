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

from vimeo_python_sdk.type.project_metadata_interactions_add_subfolder import ProjectMetadataInteractionsAddSubfolder
from vimeo_python_sdk.type.project_metadata_interactions_delete import ProjectMetadataInteractionsDelete
from vimeo_python_sdk.type.project_metadata_interactions_delete_video import ProjectMetadataInteractionsDeleteVideo
from vimeo_python_sdk.type.project_metadata_interactions_edit import ProjectMetadataInteractionsEdit
from vimeo_python_sdk.type.project_metadata_interactions_edit_settings import ProjectMetadataInteractionsEditSettings
from vimeo_python_sdk.type.project_metadata_interactions_invite import ProjectMetadataInteractionsInvite
from vimeo_python_sdk.type.project_metadata_interactions_move_video import ProjectMetadataInteractionsMoveVideo
from vimeo_python_sdk.type.project_metadata_interactions_upload_video import ProjectMetadataInteractionsUploadVideo
from vimeo_python_sdk.type.project_metadata_interactions_view import ProjectMetadataInteractionsView

class RequiredProjectMetadataInteractions(TypedDict):
    add_subfolder: ProjectMetadataInteractionsAddSubfolder

    delete: ProjectMetadataInteractionsDelete

    delete_video: ProjectMetadataInteractionsDeleteVideo

    edit: ProjectMetadataInteractionsEdit

    edit_settings: ProjectMetadataInteractionsEditSettings

    invite: ProjectMetadataInteractionsInvite

    move_video: ProjectMetadataInteractionsMoveVideo

    upload_video: ProjectMetadataInteractionsUploadVideo

    view: ProjectMetadataInteractionsView

class OptionalProjectMetadataInteractions(TypedDict, total=False):
    pass

class ProjectMetadataInteractions(RequiredProjectMetadataInteractions, OptionalProjectMetadataInteractions):
    pass

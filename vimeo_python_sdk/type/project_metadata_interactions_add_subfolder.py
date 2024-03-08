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

from vimeo_python_sdk.type.project_metadata_interactions_add_subfolder_options import ProjectMetadataInteractionsAddSubfolderOptions
from vimeo_python_sdk.type.project_metadata_interactions_add_subfolder_properties import ProjectMetadataInteractionsAddSubfolderProperties

class RequiredProjectMetadataInteractionsAddSubfolder(TypedDict):
    # Whether the folder can contain a subfolder.
    can_add_subfolders: bool

    # Whether the user has reached the maximum subfolder depth.
    subfolder_depth_limit_reached: bool

class OptionalProjectMetadataInteractionsAddSubfolder(TypedDict, total=False):
    # The subfolder content type.
    content_type: str

    options: ProjectMetadataInteractionsAddSubfolderOptions

    properties: ProjectMetadataInteractionsAddSubfolderProperties

    # The API URI that resolves to the connection data.
    uri: str

class ProjectMetadataInteractionsAddSubfolder(RequiredProjectMetadataInteractionsAddSubfolder, OptionalProjectMetadataInteractionsAddSubfolder):
    pass

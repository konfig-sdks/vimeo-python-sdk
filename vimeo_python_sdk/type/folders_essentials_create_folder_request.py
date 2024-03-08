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


class RequiredFoldersEssentialsCreateFolderRequest(TypedDict):
    # The name of the folder.
    name: str

class OptionalFoldersEssentialsCreateFolderRequest(TypedDict, total=False):
    # The URI of the parent folder.
    parent_folder_uri: str

class FoldersEssentialsCreateFolderRequest(RequiredFoldersEssentialsCreateFolderRequest, OptionalFoldersEssentialsCreateFolderRequest):
    pass

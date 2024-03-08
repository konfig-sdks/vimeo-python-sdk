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


class RequiredProjectMetadataConnectionsAncestorPathItem(TypedDict):
    # Whether the user can upload to this ancestor folder.
    can_upload: bool

    # The name of the folder.
    name: str

    # The URI of the ancestor folder.
    uri: str

class OptionalProjectMetadataConnectionsAncestorPathItem(TypedDict, total=False):
    pass

class ProjectMetadataConnectionsAncestorPathItem(RequiredProjectMetadataConnectionsAncestorPathItem, OptionalProjectMetadataConnectionsAncestorPathItem):
    pass

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


class RequiredProjectMetadataConnectionsResourceCreatorTeamUser(TypedDict):
    # The URI for the team user who created the folder. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalProjectMetadataConnectionsResourceCreatorTeamUser(TypedDict, total=False):
    pass

class ProjectMetadataConnectionsResourceCreatorTeamUser(RequiredProjectMetadataConnectionsResourceCreatorTeamUser, OptionalProjectMetadataConnectionsResourceCreatorTeamUser):
    pass

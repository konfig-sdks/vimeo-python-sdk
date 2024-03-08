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


class ProjectMetadataConnectionsResourceCreatorTeamUser(BaseModel):
    # The URI for the team user who created the folder. This data requires a bearer token with the `private` scope.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
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


class VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesFolderUri(BaseModel):
    # Whether the URI of the folder must be sent to achieve the desired action.
    required: bool = Field(alias='required')

    # The URI of the folder to which the team member should have access.
    value: str = Field(alias='value')
    class Config:
        arbitrary_types_allowed = True

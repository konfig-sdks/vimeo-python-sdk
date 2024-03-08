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


class VideoMetadataInteractionsCanRequestTeamRoleUpgradePropertiesStatus(BaseModel):
    # Whether the status of the role upgrade request must be sent to achieve the desired action.
    required: bool = Field(alias='required')

    # The status of the role upgrade request to which the team member should have access.
    value: str = Field(alias='value')
    class Config:
        arbitrary_types_allowed = True

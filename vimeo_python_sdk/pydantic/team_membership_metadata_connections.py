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

from vimeo_python_sdk.pydantic.team_membership_metadata_connections_owner import TeamMembershipMetadataConnectionsOwner
from vimeo_python_sdk.pydantic.team_membership_metadata_connections_personal_team_folder import TeamMembershipMetadataConnectionsPersonalTeamFolder

class TeamMembershipMetadataConnections(BaseModel):
    owner: TeamMembershipMetadataConnectionsOwner = Field(alias='owner')

    personal_team_folder: TeamMembershipMetadataConnectionsPersonalTeamFolder = Field(alias='personal_team_folder')
    class Config:
        arbitrary_types_allowed = True

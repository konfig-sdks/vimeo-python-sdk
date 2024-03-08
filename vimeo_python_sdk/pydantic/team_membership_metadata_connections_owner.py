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

from vimeo_python_sdk.pydantic.team_membership_metadata_connections_owner_options import TeamMembershipMetadataConnectionsOwnerOptions

class TeamMembershipMetadataConnectionsOwner(BaseModel):
    # The display name of the team owner.
    display_name: str = Field(alias='display_name')

    # The team owner's email address.
    email: str = Field(alias='email')

    # The total number of remaining team member invites.
    invites_remaining: typing.Union[int, float] = Field(alias='invites_remaining')

    options: TeamMembershipMetadataConnectionsOwnerOptions = Field(alias='options')

    # The total number of owners on this connection.
    total: typing.Union[int, float] = Field(alias='total')

    # The total number of team members for the specified team owner.
    total_members: typing.Union[int, float] = Field(alias='total_members')

    # The API URI that resolves to the connection data.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

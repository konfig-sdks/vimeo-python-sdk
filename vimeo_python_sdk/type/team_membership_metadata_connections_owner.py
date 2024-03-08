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

from vimeo_python_sdk.type.team_membership_metadata_connections_owner_options import TeamMembershipMetadataConnectionsOwnerOptions

class RequiredTeamMembershipMetadataConnectionsOwner(TypedDict):
    # The display name of the team owner.
    display_name: str

    # The team owner's email address.
    email: str

    # The total number of remaining team member invites.
    invites_remaining: typing.Union[int, float]

    options: TeamMembershipMetadataConnectionsOwnerOptions

    # The total number of owners on this connection.
    total: typing.Union[int, float]

    # The total number of team members for the specified team owner.
    total_members: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalTeamMembershipMetadataConnectionsOwner(TypedDict, total=False):
    pass

class TeamMembershipMetadataConnectionsOwner(RequiredTeamMembershipMetadataConnectionsOwner, OptionalTeamMembershipMetadataConnectionsOwner):
    pass

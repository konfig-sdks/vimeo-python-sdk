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

from vimeo_python_sdk.pydantic.permission_policy import PermissionPolicy

class TeamMembershipApplicablePermissionPolicies(BaseModel):
    # An array of folder permission policies that can apply to the team member.
    folder: typing.List[PermissionPolicy] = Field(alias='folder')

    # An array of regional delivery permission policies that can apply to the team member.
    regional_delivery: typing.List[PermissionPolicy] = Field(alias='regional_delivery')

    # An array of video permission policies that can apply to the team member.
    video: typing.List[PermissionPolicy] = Field(alias='video')
    class Config:
        arbitrary_types_allowed = True

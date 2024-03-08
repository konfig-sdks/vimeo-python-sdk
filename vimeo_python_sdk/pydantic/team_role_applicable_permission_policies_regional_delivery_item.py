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


class TeamRoleApplicablePermissionPoliciesRegionalDeliveryItem(BaseModel):
    # The translated display description of the regional delivery permission policy.
    display_description: str = Field(alias='display_description')

    # The translated display name of the regional delivery permission policy.
    display_name: str = Field(alias='display_name')

    # The name of the regional delivery permission policy.
    name: str = Field(alias='name')
    class Config:
        arbitrary_types_allowed = True

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


class PermissionPolicy(BaseModel):
    # The time at which the permission policy was created.
    created_on: str = Field(alias='created_on')

    # The display description of the permission policy, translated where applicable.
    display_description: str = Field(alias='display_description')

    # The display name of the permission policy, translated where applicable.
    display_name: str = Field(alias='display_name')

    # The time at which the permission policy was last modified.
    modified_on: typing.Optional[str] = Field(alias='modified_on')

    # The name of the permission policy.
    name: str = Field(alias='name')

    # The permission actions associated with the policy.
    permission_actions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='permission_actions')

    # The URI of the permission policy.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True

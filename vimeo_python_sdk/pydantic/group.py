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

from vimeo_python_sdk.pydantic.group_metadata import GroupMetadata
from vimeo_python_sdk.pydantic.group_privacy import GroupPrivacy
from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.user import User

class Group(BaseModel):
    # The group's description.
    description: typing.Optional[str] = Field(alias='description')

    # The time in ISO 8601 format when the group was created.
    created_time: str = Field(alias='created_time')

    # The link to the group.
    link: str = Field(alias='link')

    metadata: GroupMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the group was last modified.
    modified_time: str = Field(alias='modified_time')

    # The group's display name.
    name: str = Field(alias='name')

    # The active picture for the group.
    pictures: Picture = Field(alias='pictures')

    privacy: GroupPrivacy = Field(alias='privacy')

    # The resource key of the group.
    resource_key: str = Field(alias='resource_key')

    # The canonical relative URI of the group.
    uri: str = Field(alias='uri')

    # The owner of the group.
    user: typing.Optional[User] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True

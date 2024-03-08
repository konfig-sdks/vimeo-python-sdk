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

from vimeo_python_sdk.pydantic.project_metadata import ProjectMetadata
from vimeo_python_sdk.pydantic.project_privacy import ProjectPrivacy
from vimeo_python_sdk.pydantic.project_settings import ProjectSettings
from vimeo_python_sdk.pydantic.user import User

class Project(BaseModel):
    # The access grant response that applies to the team member. _This field is deprecated because grants are no longer exposed via API responses._
    access_grant: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='access_grant')

    # The time in ISO 8601 format when the folder was created.
    created_time: str = Field(alias='created_time')

    # The URI for the user who created the folder.
    creator_uri: str = Field(alias='creator_uri')

    # Whether this folder has at least one subfolder.
    has_subfolder: bool = Field(alias='has_subfolder')

    # Whether the folder is pinned.
    is_pinned: bool = Field(alias='is_pinned')

    # Whether the folder is a private-to-me folder for the user.
    is_private_to_user: bool = Field(alias='is_private_to_user')

    # The time in ISO 8601 format when a user last performed an action on the folder.
    last_user_action_event_date: typing.Optional[str] = Field(alias='last_user_action_event_date')

    # The link to the folder on Vimeo.
    link: str = Field(alias='link')

    # The link to the folder management page.
    manage_link: str = Field(alias='manage_link')

    metadata: ProjectMetadata = Field(alias='metadata')

    # The time in ISO 8601 format when the folder was last modified.
    modified_time: str = Field(alias='modified_time')

    # The name of the folder.
    name: str = Field(alias='name')

    # The time in ISO 8601 format when the folder was pinned.
    pinned_on: typing.Optional[str] = Field(alias='pinned_on')

    privacy: ProjectPrivacy = Field(alias='privacy')

    # The resource key string of the folder.
    resource_key: str = Field(alias='resource_key')

    settings: ProjectSettings = Field(alias='settings')

    # The URI of the folder.
    uri: str = Field(alias='uri')

    # The owner of the folder.
    user: User = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True

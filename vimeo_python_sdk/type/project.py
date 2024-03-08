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

from vimeo_python_sdk.type.project_metadata import ProjectMetadata
from vimeo_python_sdk.type.project_privacy import ProjectPrivacy
from vimeo_python_sdk.type.project_settings import ProjectSettings
from vimeo_python_sdk.type.user import User

class RequiredProject(TypedDict):
    # The access grant response that applies to the team member. _This field is deprecated because grants are no longer exposed via API responses._
    access_grant: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The time in ISO 8601 format when the folder was created.
    created_time: str

    # The URI for the user who created the folder.
    creator_uri: str

    # Whether this folder has at least one subfolder.
    has_subfolder: bool

    # Whether the folder is pinned.
    is_pinned: bool

    # Whether the folder is a private-to-me folder for the user.
    is_private_to_user: bool

    # The time in ISO 8601 format when a user last performed an action on the folder.
    last_user_action_event_date: typing.Optional[str]

    # The link to the folder on Vimeo.
    link: str

    # The link to the folder management page.
    manage_link: str

    metadata: ProjectMetadata

    # The time in ISO 8601 format when the folder was last modified.
    modified_time: str

    # The name of the folder.
    name: str

    # The time in ISO 8601 format when the folder was pinned.
    pinned_on: typing.Optional[str]

    privacy: ProjectPrivacy

    # The resource key string of the folder.
    resource_key: str

    settings: ProjectSettings

    # The URI of the folder.
    uri: str

    # The owner of the folder.
    user: User

class OptionalProject(TypedDict, total=False):
    pass

class Project(RequiredProject, OptionalProject):
    pass

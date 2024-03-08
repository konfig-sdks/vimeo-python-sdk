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

from vimeo_python_sdk.type.group_metadata import GroupMetadata
from vimeo_python_sdk.type.group_privacy import GroupPrivacy
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.user import User

class RequiredGroup(TypedDict):
    # The group's description.
    description: typing.Optional[str]

    # The time in ISO 8601 format when the group was created.
    created_time: str

    # The link to the group.
    link: str

    metadata: GroupMetadata

    # The time in ISO 8601 format when the group was last modified.
    modified_time: str

    # The group's display name.
    name: str

    # The active picture for the group.
    pictures: Picture

    privacy: GroupPrivacy

    # The resource key of the group.
    resource_key: str

    # The canonical relative URI of the group.
    uri: str

class OptionalGroup(TypedDict, total=False):
    # The owner of the group.
    user: User

class Group(RequiredGroup, OptionalGroup):
    pass

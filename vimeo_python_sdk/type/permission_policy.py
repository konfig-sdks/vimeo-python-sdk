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


class RequiredPermissionPolicy(TypedDict):
    # The time at which the permission policy was created.
    created_on: str

    # The display description of the permission policy, translated where applicable.
    display_description: str

    # The display name of the permission policy, translated where applicable.
    display_name: str

    # The time at which the permission policy was last modified.
    modified_on: typing.Optional[str]

    # The name of the permission policy.
    name: str

    # The permission actions associated with the policy.
    permission_actions: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The URI of the permission policy.
    uri: str

class OptionalPermissionPolicy(TypedDict, total=False):
    pass

class PermissionPolicy(RequiredPermissionPolicy, OptionalPermissionPolicy):
    pass

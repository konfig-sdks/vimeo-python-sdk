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


class RequiredVideoContext(TypedDict):
    # The relevant contextual action.  Option descriptions:  * `Added to` - An Added To action.  * `Appearance by` - An Appearance By action.  * `Liked by` - A Liked By action.  * `Uploaded by` - An Uploaded By action. 
    action: str

    # The contextual resource: a user, group, or channel representation, or an object of a tag.
    resource: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # The contextual resource type.
    resource_type: str

class OptionalVideoContext(TypedDict, total=False):
    pass

class VideoContext(RequiredVideoContext, OptionalVideoContext):
    pass

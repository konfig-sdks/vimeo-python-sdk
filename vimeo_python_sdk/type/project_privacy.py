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


class RequiredProjectPrivacy(TypedDict):
    # The privacy setting for accessing the folder.  Option descriptions:  * `anybody` - Anyone with the link can access the contents of the folder. This privacy setting appears as `Public` on the Vimeo front end.  * `nobody` - Only the owner and those team members that the owner has explicitly invited can access the contents of the folder. This privacy setting appears as `Private` on the Vimeo front end.  * `team` - Only those team members with the link can access the contents of the folder. 
    view: str

class OptionalProjectPrivacy(TypedDict, total=False):
    pass

class ProjectPrivacy(RequiredProjectPrivacy, OptionalProjectPrivacy):
    pass

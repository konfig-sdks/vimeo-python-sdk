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


class RequiredGroupPrivacy(TypedDict):
    # Who can comment on the group.  Option descriptions:  * `all` - Anyone can comment on the group.  * `members` - Only group members can comment on the group. 
    comment: str

    # Who can invite new members to the group.  Option descriptions:  * `all` - Anyone can invite new members to the group.  * `members` - Only group members can invite new members to the group. 
    invite: str

    # Who can join the group.  Option descriptions:  * `anybody` - Anyone can join the group.  * `members` - Only people with a Vimeo account can join the group. 
    join: str

    # Who can add videos to the group.  Option descriptions:  * `all` - Anyone can add videos to the group.  * `members` - Only group members can add videos to the group. 
    videos: str

    # Who can access the group.  Option descriptions:  * `anybody` - Anyone can access the group. This privacy setting appears as `Public` on the Vimeo front end.  * `members` - Only group members can access the group. 
    view: str

class OptionalGroupPrivacy(TypedDict, total=False):
    pass

class GroupPrivacy(RequiredGroupPrivacy, OptionalGroupPrivacy):
    pass

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

from vimeo_python_sdk.type.activity31_metadata import Activity31Metadata
from vimeo_python_sdk.type.category import Category
from vimeo_python_sdk.type.channel import Channel
from vimeo_python_sdk.type.group import Group
from vimeo_python_sdk.type.tag import Tag
from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.video import Video

class RequiredActivity31(TypedDict):
    # The video associated with the activity.
    clip: Video

    metadata: Activity31Metadata

    # The time that the event occurred.
    time: str

    # The activity type.  Option descriptions:  * `appearance` - The activity is an appearance action.  * `category` - The activity is a category action.  * `channel` - The activity is a channel action.  * `facebook_feed` - The activity is a Facebook feed action.  * `group` - The activity is a group action.  * `like` - The activity is a like action.  * `ondemand` - The activity is a Vimeo On Demand action.  * `share` - The activity is a share action.  * `tag` - The activity is a tag action.  * `twitter_timeline` - The activity is a Twitter timeline action.  * `upload` - The activity is an upload action. 
    type: str

class OptionalActivity31(TypedDict, total=False):
    # The category associated with the event. This field is present only when the activity type is `category`.
    category: Category

    # The channel associated with the event. This field is present only when the activity type is `channel`.
    channel: Channel

    # The group associated with the event. This field is present only when the activity type is `group`.
    group: Group

    # The tag associated with the event. This field is present only when the activity type is `tag`.
    tag: Tag

    # The user associated with the event. This field is present only when the activity type is `like`, `appearance`, or `share`.
    user: User

class Activity31(RequiredActivity31, OptionalActivity31):
    pass

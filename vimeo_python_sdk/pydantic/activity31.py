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

from vimeo_python_sdk.pydantic.activity31_metadata import Activity31Metadata
from vimeo_python_sdk.pydantic.category import Category
from vimeo_python_sdk.pydantic.channel import Channel
from vimeo_python_sdk.pydantic.group import Group
from vimeo_python_sdk.pydantic.tag import Tag
from vimeo_python_sdk.pydantic.user import User
from vimeo_python_sdk.pydantic.video import Video

class Activity31(BaseModel):
    # The video associated with the activity.
    clip: Video = Field(alias='clip')

    metadata: Activity31Metadata = Field(alias='metadata')

    # The time that the event occurred.
    time: str = Field(alias='time')

    # The activity type.  Option descriptions:  * `appearance` - The activity is an appearance action.  * `category` - The activity is a category action.  * `channel` - The activity is a channel action.  * `facebook_feed` - The activity is a Facebook feed action.  * `group` - The activity is a group action.  * `like` - The activity is a like action.  * `ondemand` - The activity is a Vimeo On Demand action.  * `share` - The activity is a share action.  * `tag` - The activity is a tag action.  * `twitter_timeline` - The activity is a Twitter timeline action.  * `upload` - The activity is an upload action. 
    type: Literal["appearance", "category", "channel", "facebook_feed", "group", "like", "ondemand", "share", "tag", "twitter_timeline", "upload"] = Field(alias='type')

    # The category associated with the event. This field is present only when the activity type is `category`.
    category: typing.Optional[Category] = Field(None, alias='category')

    # The channel associated with the event. This field is present only when the activity type is `channel`.
    channel: typing.Optional[Channel] = Field(None, alias='channel')

    # The group associated with the event. This field is present only when the activity type is `group`.
    group: typing.Optional[Group] = Field(None, alias='group')

    # The tag associated with the event. This field is present only when the activity type is `tag`.
    tag: typing.Optional[Tag] = Field(None, alias='tag')

    # The user associated with the event. This field is present only when the activity type is `like`, `appearance`, or `share`.
    user: typing.Optional[User] = Field(None, alias='user')
    class Config:
        arbitrary_types_allowed = True

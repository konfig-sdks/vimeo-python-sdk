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

from vimeo_python_sdk.pydantic.users_essentials_edit_vimeo_account_request_content_filter import UsersEssentialsEditVimeoAccountRequestContentFilter
from vimeo_python_sdk.pydantic.users_essentials_edit_vimeo_account_request_videos import UsersEssentialsEditVimeoAccountRequestVideos

class UsersEssentialsEditVimeoAccountRequest(BaseModel):
    # The user's bio.
    bio: typing.Optional[str] = Field(None, alias='bio')

    content_filter: typing.Optional[UsersEssentialsEditVimeoAccountRequestContentFilter] = Field(None, alias='content_filter')

    # The authenticated user's gender.  Option descriptions:  * `f` - The user's preferred pronouns are she and her.  * `m` - The user's preferred pronouns are he and him.  * `n` - The user would rather not give preferred pronouns.  * `o` - The user's preferred pronouns are they and them. 
    gender: typing.Optional[Literal["f", "m", "n", "o"]] = Field(None, alias='gender')

    # The user's custom Vimeo URL.
    link: typing.Optional[str] = Field(None, alias='link')

    # The user's location.
    location: typing.Optional[str] = Field(None, alias='location')

    # The user's display name.
    name: typing.Optional[str] = Field(None, alias='name')

    # The default password for all future videos that this user uploads. To use this field, the **videos.privacy.view** field must be `password`.
    password: typing.Optional[str] = Field(None, alias='password')

    videos: typing.Optional[UsersEssentialsEditVimeoAccountRequestVideos] = Field(None, alias='videos')
    class Config:
        arbitrary_types_allowed = True

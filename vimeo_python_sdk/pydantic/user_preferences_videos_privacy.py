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


class UserPreferencesVideosPrivacy(BaseModel):
    # Whether other users can add the authenticated user's videos.
    add: typing.Optional[bool] = Field(None, alias='add')

    # The authenticated user's privacy preference for comments.  Option descriptions:  * `anybody` - Anyone can comment on the user's videos.  * `contacts` - Only contacts can comment on the user's videos.  * `nobody` - No one can comment on the user's videos. 
    comments: typing.Optional[Literal["anybody", "contacts", "nobody"]] = Field(None, alias='comments')

    # Whether other users can download the authenticated user's videos.
    download: typing.Optional[bool] = Field(None, alias='download')

    # The authenticated user's privacy preference for embeds.  Option descriptions:  * `private` - Only the user can embed their own videos.  * `public` - Anyone can embed the user's videos.  * `whitelist` - Only those on the whitelist can embed the user's videos. 
    embed: typing.Optional[Literal["private", "public", "whitelist"]] = Field(None, alias='embed')

    # The default password for the video.
    password: typing.Optional[str] = Field(None, alias='password')

    # The authenticated user's privacy preference for views.  Option descriptions:  * `anybody` - Anyone can view the user's videos. This privacy setting appears as `Public` on the Vimeo front end.  * `contacts` - Only contacts can view the user's videos. _This field is deprecated._  * `disable` - Views are disabled for the user's videos. This privacy setting appears as `Hide from Vimeo` on the Vimeo front end.  * `nobody` - No one except the user can view the user's videos. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can view the user's videos.  * `unlisted` - Anybody can view the user's videos if they have a link.  * `users` - Only other Vimeo members can view the user's videos. _This field is deprecated._ 
    view: typing.Optional[Literal["anybody", "contacts", "disable", "nobody", "password", "unlisted", "users"]] = Field(None, alias='view')
    class Config:
        arbitrary_types_allowed = True

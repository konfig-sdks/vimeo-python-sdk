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


class VideosUploadsBeginVideoUploadProcessRequestPrivacy(BaseModel):
    # Whether a user can add the video to a showcase, channel, or group.
    add: typing.Optional[bool] = Field(None, alias='add')

    # The privacy level required to comment on the video.  Option descriptions:  * `anybody` - Anyone can comment on the video.  * `contacts` - Only the video owner's contacts can comment on the video.  * `nobody` - No one can comment on the video. 
    comments: typing.Optional[Literal["anybody", "contacts", "nobody"]] = Field(None, alias='comments')

    # Whether a user can download the video. This field isn't available to Vimeo Free members.
    download: typing.Optional[bool] = Field(None, alias='download')

    # The video's embed setting. Specify the `whitelist` value to restrict embedding to a specific set of domains. For more information, see our [Interacting with Videos](https://developer.vimeo.com/api/guides/videos/interact#set-off-site-privacy) guide.  Option descriptions:  * `private` - The video can't be embedded.  * `public` - The video can be embedded.  * `whitelist` - The video can be embedded on the specified domains only. 
    embed: typing.Optional[Literal["private", "public", "whitelist"]] = Field(None, alias='embed')

    # The video's privacy setting. When this value is `users`, `application/json` is the only valid content type. Also, some privacy settings are unavailable to Vimeo Free members; for more information, see our [Help Center](https://vimeo.zendesk.com/hc/en-us/articles/224817847).  Option descriptions:  * `anybody` - Anyone can access the video. This privacy setting appears as `Public` on the Vimeo front end.  * `contacts` - Only those who follow the owner on Vimeo can access the video. _This field is deprecated._  * `disable` - The video is embeddable, but it's hidden on Vimeo and can't be played. This privacy setting appears as `Hide from Vimeo` on the Vimeo front end. _This field is deprecated._  * `nobody` - No one except the owner can access the video. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the video.  * `unlisted` - Only those with the private link can access the video.  * `users` - Only Vimeo members can access the video. _This field is deprecated._ 
    view: typing.Optional[Literal["anybody", "contacts", "disable", "nobody", "password", "unlisted", "users"]] = Field(None, alias='view')
    class Config:
        arbitrary_types_allowed = True

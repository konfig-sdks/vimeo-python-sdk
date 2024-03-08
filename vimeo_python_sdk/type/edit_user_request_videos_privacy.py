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


class RequiredEditUserRequestVideosPrivacy(TypedDict):
    pass

class OptionalEditUserRequestVideosPrivacy(TypedDict, total=False):
    # Whether the user can add videos to showcases, channels, or groups by default.
    add: bool

    # Who can comment on the user's video uploads by default.  Option descriptions:  * `anybody` - Anyone can comment.  * `contacts` - Only the user's contacts can comment.  * `nobody` - No one can comment. 
    comments: str

    # Whether the user can download videos. This value becomes the default download setting for all future videos that the user uploads.
    download: bool

    # The privacy for the user's embedded videos. The whitelist value enables you to define all valid embeddable domains. See our [Interacting with Videos](https://developer.vimeo.com/api/guides/videos/interact#set-off-site-privacy) guide for details on adding and removing domains.  Option descriptions:  * `private` - The videos can't be embedded on any domain.  * `public` - The videos can be embedded on any domain.  * `whitelist` - The videos can be embedded on the specified domains only. 
    embed: str

    # Who can access the user's videos by default.  Option descriptions:  * `anybody` - Anyone can access the videos. This privacy setting appears as `Public` on the Vimeo front end.  * `contacts` - Only the user's contacts can access the videos. _This field is deprecated._  * `disable` - The videos are disabled. This privacy setting appears as `Hide from Vimeo` on the Vimeo front end.  * `nobody` - No one can access the videos. This privacy setting appears as `Private` on the Vimeo front end.  * `password` - Only those with the password can access the videos.  * `unlisted` - The videos are unlisted.  * `users` - Only other Vimeo members can access the videos. _This field is deprecated._ 
    view: str

class EditUserRequestVideosPrivacy(RequiredEditUserRequestVideosPrivacy, OptionalEditUserRequestVideosPrivacy):
    pass

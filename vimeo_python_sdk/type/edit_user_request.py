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

from vimeo_python_sdk.type.edit_user_request_content_filter import EditUserRequestContentFilter
from vimeo_python_sdk.type.edit_user_request_videos import EditUserRequestVideos

class RequiredEditUserRequest(TypedDict):
    pass

class OptionalEditUserRequest(TypedDict, total=False):
    # The user's bio.
    bio: str

    content_filter: EditUserRequestContentFilter

    # The authenticated user's gender.  Option descriptions:  * `f` - The user's preferred pronouns are she and her.  * `m` - The user's preferred pronouns are he and him.  * `n` - The user would rather not give preferred pronouns.  * `o` - The user's preferred pronouns are they and them. 
    gender: str

    # The user's custom Vimeo URL.
    link: str

    # The user's location.
    location: str

    # The user's display name.
    name: str

    # The default password for all future videos that this user uploads. To use this field, the **videos.privacy.view** field must be `password`.
    password: str

    videos: EditUserRequestVideos

class EditUserRequest(RequiredEditUserRequest, OptionalEditUserRequest):
    pass

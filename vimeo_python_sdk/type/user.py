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

from vimeo_python_sdk.type.location import Location
from vimeo_python_sdk.type.picture import Picture
from vimeo_python_sdk.type.skill import Skill
from vimeo_python_sdk.type.user_content_filter import UserContentFilter
from vimeo_python_sdk.type.user_metadata import UserMetadata
from vimeo_python_sdk.type.user_preferences import UserPreferences
from vimeo_python_sdk.type.user_upload_quota import UserUploadQuota
from vimeo_python_sdk.type.user_websites import UserWebsites

class RequiredUser(TypedDict):
    # The authenticated user's account type.  Option descriptions:  * `advanced` - The user has a Vimeo Advanced subscription.  * `basic` - The user has a Vimeo Basic subscription.  * `business` - The user has a Vimeo Business subscription.  * `enterprise` - The user has a Vimeo Enterprise subscription.  * `free` - The user has a Vimeo Free subscription.  * `live_business` - The user has a Vimeo Business Live subscription.  * `live_premium` - The user has a Vimeo Premium subscription.  * `live_pro` - The user has a Vimeo PRO Live subscription.  * `plus` - The user has a Vimeo Plus subscription.  * `pro` - The user has a Vimeo Pro subscription.  * `pro_unlimited` - The user has a Vimeo PRO Unlimited subscription.  * `producer` - The user has a Vimeo Producer subscription.  * `standard` - The user has a Vimeo Standard subscription.  * `starter` - The user has a Vimeo Starter subscription. 
    account: str

    # Whether the authenticated user is available for hire.
    available_for_hire: bool

    # The authenticated user's long bio text.
    bio: typing.Optional[str]

    # Whether the authenticated user can work remotely.
    can_work_remotely: bool

    # The users's capabilities list.
    capabilities: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The comma-separated list of clients.
    clients: str

    # The time in ISO 8601 format when the user account was created.
    created_time: str

    # The authenticated user's gender.
    gender: typing.Optional[str]

    # Whether the user's email is invalid.
    has_invalid_email: bool

    # Whether the creator enrolled in and successfully completed the Vimeo Experts program.
    is_expert: bool

    # The absolute URL of the authenticated users's profile page.
    link: str

    # The authenticated user's location.
    location: typing.Optional[str]

    # The authenticated user's location details.
    location_details: Location

    metadata: UserMetadata

    # The authenticated user's display name.
    name: str

    # The active portrait of the authenticated user.
    pictures: Picture

    preferences: UserPreferences

    # The authenticated user's resource key string.
    resource_key: str

    # The authenticated user's short bio text.
    short_bio: typing.Optional[str]

    # A list of the authenticated user's skills.
    skills: typing.Optional[typing.List[Skill]]

    upload_quota: UserUploadQuota

    # The authenticated user's canonical relative URI.
    uri: str

    websites: UserWebsites

class OptionalUser(TypedDict, total=False):
    content_filter: UserContentFilter

class User(RequiredUser, OptionalUser):
    pass

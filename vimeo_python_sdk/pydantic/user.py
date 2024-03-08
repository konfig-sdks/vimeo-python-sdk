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

from vimeo_python_sdk.pydantic.location import Location
from vimeo_python_sdk.pydantic.picture import Picture
from vimeo_python_sdk.pydantic.skill import Skill
from vimeo_python_sdk.pydantic.user_content_filter import UserContentFilter
from vimeo_python_sdk.pydantic.user_metadata import UserMetadata
from vimeo_python_sdk.pydantic.user_preferences import UserPreferences
from vimeo_python_sdk.pydantic.user_upload_quota import UserUploadQuota
from vimeo_python_sdk.pydantic.user_websites import UserWebsites

class User(BaseModel):
    # The authenticated user's account type.  Option descriptions:  * `advanced` - The user has a Vimeo Advanced subscription.  * `basic` - The user has a Vimeo Basic subscription.  * `business` - The user has a Vimeo Business subscription.  * `enterprise` - The user has a Vimeo Enterprise subscription.  * `free` - The user has a Vimeo Free subscription.  * `live_business` - The user has a Vimeo Business Live subscription.  * `live_premium` - The user has a Vimeo Premium subscription.  * `live_pro` - The user has a Vimeo PRO Live subscription.  * `plus` - The user has a Vimeo Plus subscription.  * `pro` - The user has a Vimeo Pro subscription.  * `pro_unlimited` - The user has a Vimeo PRO Unlimited subscription.  * `producer` - The user has a Vimeo Producer subscription.  * `standard` - The user has a Vimeo Standard subscription.  * `starter` - The user has a Vimeo Starter subscription. 
    account: Literal["advanced", "basic", "business", "enterprise", "free", "live_business", "live_premium", "live_pro", "plus", "pro", "pro_unlimited", "producer", "standard", "starter"] = Field(alias='account')

    # Whether the authenticated user is available for hire.
    available_for_hire: bool = Field(alias='available_for_hire')

    # The authenticated user's long bio text.
    bio: typing.Optional[str] = Field(alias='bio')

    # Whether the authenticated user can work remotely.
    can_work_remotely: bool = Field(alias='can_work_remotely')

    # The users's capabilities list.
    capabilities: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='capabilities')

    # The comma-separated list of clients.
    clients: str = Field(alias='clients')

    # The time in ISO 8601 format when the user account was created.
    created_time: str = Field(alias='created_time')

    # The authenticated user's gender.
    gender: typing.Optional[str] = Field(alias='gender')

    # Whether the user's email is invalid.
    has_invalid_email: bool = Field(alias='has_invalid_email')

    # Whether the creator enrolled in and successfully completed the Vimeo Experts program.
    is_expert: bool = Field(alias='is_expert')

    # The absolute URL of the authenticated users's profile page.
    link: str = Field(alias='link')

    # The authenticated user's location.
    location: typing.Optional[str] = Field(alias='location')

    # The authenticated user's location details.
    location_details: Location = Field(alias='location_details')

    metadata: UserMetadata = Field(alias='metadata')

    # The authenticated user's display name.
    name: str = Field(alias='name')

    # The active portrait of the authenticated user.
    pictures: Picture = Field(alias='pictures')

    preferences: UserPreferences = Field(alias='preferences')

    # The authenticated user's resource key string.
    resource_key: str = Field(alias='resource_key')

    # The authenticated user's short bio text.
    short_bio: typing.Optional[str] = Field(alias='short_bio')

    # A list of the authenticated user's skills.
    skills: typing.Optional[typing.List[Skill]] = Field(alias='skills')

    upload_quota: UserUploadQuota = Field(alias='upload_quota')

    # The authenticated user's canonical relative URI.
    uri: str = Field(alias='uri')

    websites: UserWebsites = Field(alias='websites')

    content_filter: typing.Optional[UserContentFilter] = Field(None, alias='content_filter')
    class Config:
        arbitrary_types_allowed = True

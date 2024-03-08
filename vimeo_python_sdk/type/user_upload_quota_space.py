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


class RequiredUserUploadQuotaSpace(TypedDict):
    # The number of bytes or videos remaining in the authenticated user's upload quota.
    free: typing.Union[int, float]

    # The maximum number of bytes or videos allotted to the authenticated user's upload quota.
    max: typing.Optional[typing.Union[int, float]]

    # The type of quota for the values of the **upload_quota.space** field.  Option descriptions:  * `lifetime` - The quota type is lifetime.  * `periodic` - The quota type is periodic. 
    showing: str

    # The unit that's used to compute quota.  Option descriptions:  * `video_count` - The quota is calculated using the count of the videos.  * `video_size` - The quota is calculated using the byte size of the videos. 
    unit: typing.Optional[str]

    # The number of bytes or videos that the authenticated user has already uploaded against their quota.
    used: typing.Union[int, float]

class OptionalUserUploadQuotaSpace(TypedDict, total=False):
    pass

class UserUploadQuotaSpace(RequiredUserUploadQuotaSpace, OptionalUserUploadQuotaSpace):
    pass

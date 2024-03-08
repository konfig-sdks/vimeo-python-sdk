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


class RequiredSubscriptionPlansMetadataEntitlementsParams(TypedDict):
    # The number of team seats included with the tier.
    team_seats: typing.Optional[str]

    # The amount of video storage for the user's periodic quota.
    video_storage_periodic_quota: typing.Optional[str]

    # The video storage total lifetime cap.
    video_storage_quota_cap: typing.Optional[str]

    # The video storage quota period.  Option descriptions:  * `lifetime` - The product has a lifetime video storage quota period.  * `month` - The product has a monthly video storage quota period.  * `week` - The product has a weekly video storage quota period.  * `year` - The product has a yearly video storage quota period. 
    video_storage_quota_period: str

    # The unit of the video storage for the user's periodic quota.  Option descriptions:  * `video_count` - The product has video storage based on video count.  * `video_size` - The product has video storage based on video size. 
    video_storage_quota_unit: str

class OptionalSubscriptionPlansMetadataEntitlementsParams(TypedDict, total=False):
    pass

class SubscriptionPlansMetadataEntitlementsParams(RequiredSubscriptionPlansMetadataEntitlementsParams, OptionalSubscriptionPlansMetadataEntitlementsParams):
    pass

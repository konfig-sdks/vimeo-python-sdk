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

from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request2_schedule_weekdays import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2ScheduleWeekdays

class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Schedule(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Schedule(TypedDict, total=False):
    # The time in ISO 8601 format when the event is expected to be live, with the zero UTC offset `Z`. This parameter is required when **schedule.type** is `weekly`.
    daily_time: str

    # How often the event is expected to be live.  Option descriptions:  * `single` - The event is live one time only.  * `weekly` - The event is live on a weekly basis. 
    type: str

    weekdays: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2ScheduleWeekdays

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Schedule(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Schedule, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2Schedule):
    pass

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

from vimeo_python_sdk.type.webinar_essentials_create_webinar_request_schedule_weekdays import WebinarEssentialsCreateWebinarRequestScheduleWeekdays

class RequiredWebinarEssentialsCreateWebinarRequestSchedule(TypedDict):
    pass

class OptionalWebinarEssentialsCreateWebinarRequestSchedule(TypedDict, total=False):
    # The time in ISO 8601 format when the webinar is expected to be live, with the zero UTC offset `Z`. This parameter is required when **schedule.type** is `weekly`. _This field is deprecated._
    daily_time: str

    # The time in ISO 8601 format when the webinar is expected to end, with support for different time offsets. This parameter is required when **schedule.type** is `single`.
    end_time: str

    # The time in ISO 8601 format when the webinar is expected to be live, with support for different time offsets. This parameter is required when **schedule.type** is `single`.
    start_time: str

    # How often the webinar is expected to be live.  Option descriptions:  * `single` - The webinar is live one time only.  * `weekly` - The webinar is live on a weekly basis. _This field is deprecated._ 
    type: str

    weekdays: WebinarEssentialsCreateWebinarRequestScheduleWeekdays

class WebinarEssentialsCreateWebinarRequestSchedule(RequiredWebinarEssentialsCreateWebinarRequestSchedule, OptionalWebinarEssentialsCreateWebinarRequestSchedule):
    pass

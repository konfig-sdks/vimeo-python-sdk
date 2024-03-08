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

from vimeo_python_sdk.type.webinar_schedule_weekdays import WebinarScheduleWeekdays

class RequiredWebinarSchedule(TypedDict):
    # The time in ISO 8601 format at which the webinar is expected to be live when **schedule.type** is `weekly`.
    daily_time: str

    # The date in ISO 8601 format on which the webinar is expected to end. This field applies when **schedule.type** is `single`.
    end_time: str

    # The date in ISO 8601 format on which the first occurrence of the webinar is expected to be live when **schedule.type** is `weekly`.
    scheduled_time: typing.Optional[str]

    # The date in ISO 8601 format on which the webinar is expected to be live when **schedule.type** is `single`.
    start_time: str

    # The schedule of the webinar.  Option descriptions:  * `single` - The webinar is live only once.  * `weekly` - The webinar is live on a recurring weekly basis. 
    type: str

    weekdays: WebinarScheduleWeekdays

class OptionalWebinarSchedule(TypedDict, total=False):
    pass

class WebinarSchedule(RequiredWebinarSchedule, OptionalWebinarSchedule):
    pass
